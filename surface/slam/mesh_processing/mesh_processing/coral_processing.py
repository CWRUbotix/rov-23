from threading import Thread

import numpy
import numpy as np
import open3d as o3d

import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
import sensor_msgs.msg as sensor_msgs

from convert_pointcloud import read_points


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

        pcd_as_numpy_array = np.array(list(read_points(msg)))

        self.pcd = o3d.geometry.PointCloud(
            o3d.utility.Vector3dVector(pcd_as_numpy_array[:, :3]))
        # Add the rgb colors, converting from rgb to bgr by flipping
        self.pcd.colors = o3d.utility.Vector3dVector(numpy.flip(pcd_as_numpy_array[:, 3:], axis=1) / 255.0)

        self.pcd.estimate_normals()
        self.pcd.orient_normals_consistent_tangent_plane(100)
        self.mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd=self.pcd, depth=9)

        # Visualize the pointcloud
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)


def main(args=None):
    # Boilerplate code.
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
