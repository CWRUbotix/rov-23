import copy
from threading import Thread
import os

import numpy
import numpy as np
import open3d as o3d

import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
import sensor_msgs.msg as sensor_msgs
from ament_index_python.packages import get_package_share_directory

import math
import struct
from sensor_msgs.msg import PointCloud2

WHITE_SQUARE_BRIGHTNESS_CUTOFF = 0.6

# find the surface/slam directory
parent = os.path.dirname
output_file_path = os.path.join(get_package_share_directory("coral_viewer"),
                                "coral_viewer_unity", "Build", "coral_viewer_Data", "StreamingAssets",
                                "coral_output.obj")


def postprocess_mesh(mesh: o3d.geometry.TriangleMesh):
    # Remove unconnected components
    triangle_clusters, cluster_n_triangles, cluster_area = mesh.cluster_connected_triangles()
    cluster_n_triangles = np.asarray(cluster_n_triangles)
    largest_cluster_idx = cluster_n_triangles.argmax()
    triangles_to_remove = triangle_clusters != largest_cluster_idx
    mesh.remove_triangles_by_mask(triangles_to_remove)


def measure_white_area(mesh: o3d.geometry.TriangleMesh) -> float:
    colors = numpy.asarray(mesh.vertex_colors)
    masked_mesh = copy.deepcopy(mesh)
    masked_mesh.remove_vertices_by_mask(np.average(colors, axis=1) < WHITE_SQUARE_BRIGHTNESS_CUTOFF)

    # return masked_mesh.get_surface_area()
    print(masked_mesh.get_surface_area())
    return masked_mesh


class PCDListener(Node):

    def __init__(self):
        super().__init__('pointcloud_subsriber_node')

        # This is for visualization of the received point cloud.
        self.vis = o3d.visualization.Visualizer()
        self.vis.create_window()
        self.pcd = o3d.geometry.PointCloud()
        self.mesh = o3d.geometry.TriangleMesh()

        # Set up a subscription to the 'pcd' topic with a callback to the
        # function `listener_callback`
        self.pcd_subscriber = self.create_subscription(
            sensor_msgs.PointCloud2,  # Msg type
            '/cloud_map',  # topic
            self.listener_callback,  # Function to call
            10  # QoS
        )

    def listener_callback(self, msg):
        print("Revieced msg")

        pcd_as_numpy_array = get_pointcloud(msg)

        self.pcd = o3d.geometry.PointCloud(
            o3d.utility.Vector3dVector(pcd_as_numpy_array[:, :3]))
        # Add the rgb colors, converting from rgb to bgr by flipping
        self.pcd.colors = o3d.utility.Vector3dVector(numpy.flip(pcd_as_numpy_array[:, 3:], axis=1) / 255.0)

        self.pcd.estimate_normals()
        self.pcd.orient_normals_to_align_with_direction([0, 1, 0])
        self.mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd=self.pcd, depth=9)

        postprocess_mesh(self.mesh)

        # Visualize the mesh
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.25))

        # export mesh
        o3d.io.write_triangle_mesh(output_file_path, self.mesh,
                                   write_triangle_uvs=False,
                                   write_vertex_colors=True)

        #  Give the obj file a txt extension so it can be parsed manually in unity
        #  This is necessary because the obj standard doesn't include colors, so the open3d output isn't a proper obj
        try:
            os.remove(output_file_path + ".txt")
        except FileNotFoundError:
            pass
        os.rename(output_file_path, output_file_path + ".txt")


def read_points(cloud, field_names=None, skip_nans=False, uvs=[]):
    """
    Read points from a L{sensor_msgs.PointCloud2} message.
    @param cloud: The point cloud to read from.
    @type  cloud: L{sensor_msgs.PointCloud2}
    @param field_names: The names of fields to read. If None, read all fields. [default: None]
    @type  field_names: iterable
    @param skip_nans: If True, then don't return any point with a NaN value.
    @type  skip_nans: bool [default: False]
    @param uvs: If specified, then only return the points at the given coordinates. [default: empty list]
    @type  uvs: iterable
    @return: Generator which yields a list of values for each point.
    @rtype:  generator
    """
    assert isinstance(cloud, PointCloud2), 'cloud is not a sensor_msgs.msg.PointCloud2'
    fmt = "<fffxxxxBBB"
    width, height, point_step, row_step, data, isnan = cloud.width, cloud.height, cloud.point_step, cloud.row_step, \
                                                       cloud.data, math.isnan
    unpack_from = struct.Struct(fmt).unpack_from

    if skip_nans:
        if uvs:
            for u, v in uvs:
                p = unpack_from(data, (row_step * v) + (point_step * u))
                has_nan = False
                for pv in p:
                    if isnan(pv):
                        has_nan = True
                        break
                if not has_nan:
                    yield p
        else:
            for v in range(height):
                offset = row_step * v
                for u in range(width):
                    p = unpack_from(data, offset)
                    has_nan = False
                    for pv in p:
                        if isnan(pv):
                            has_nan = True
                            break
                    if not has_nan:
                        yield p
                    offset += point_step
    else:
        if uvs:
            for u, v in uvs:
                yield unpack_from(data, (row_step * v) + (point_step * u))
        else:
            for v in range(height):
                offset = row_step * v
                for u in range(width):
                    yield unpack_from(data, offset)
                    offset += point_step


def get_pointcloud(msg):
    pcd = np.array(list(read_points(msg)))
    # Transform from ROS coordinates to Open3d coordinates
    transform_mat = np.matrix('0 -1 0; 0 0 -1; 1 0 0')
    return np.append(pcd[:, :3].dot(transform_mat), pcd[:, 3:], axis=1)


def main(args=None):
    rclpy.init(args=args)
    pcd_listener = PCDListener()
    custom_executor = SingleThreadedExecutor()
    custom_executor.add_node(pcd_listener)
    Thread(target=custom_executor.spin, daemon=True,
           name="coral_spinner").start()

    pcd_listener.vis.run()


def kill_executor(self):
    self.custom_executor.shutdown()


if __name__ == '__main__':
    main()
