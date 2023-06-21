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

from convert_pointcloud import get_pointcloud

WHITE_SQUARE_BRIGHTNESS_CUTOFF = 0.6

# find the surface/slam directory
parent = os.path.dirname
output_file_path = os.path.join(str(os.path.realpath(__file__)).split("slam")[0],
                                "slam", "coral_viewer", "Build", "coral_viewer_Data", "StreamingAssets",
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


def main(args=None):
    rclpy.init(args=args)
    pcd_listener = PCDListener()
    custom_executor = SingleThreadedExecutor()
    custom_executor.add_node(pcd_listener)
    Thread(target=custom_executor.spin, daemon=True,
           name="coral_spinner").start()

    while True:
        pcd_listener.vis.poll_events()
        pcd_listener.vis.update_renderer()


def kill_executor(self):
    self.custom_executor.shutdown()


if __name__ == '__main__':
    main()
