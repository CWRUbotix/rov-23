import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command

NS = "simulation"


def generate_launch_description():
    rov_gazebo_path: str = get_package_share_directory("rov_gazebo")
    ros_ign_gazebo_path: str = get_package_share_directory("ros_ign_gazebo")
    surface_main_path: str = get_package_share_directory("surface_main")

    world_path: str = os.path.join(rov_gazebo_path, "worlds", "world.sdf")

    # Process the URDF file
    xacro_file = os.path.join(rov_gazebo_path, "description", "rov.xacro")
    robot_description = Command(["xacro ", xacro_file])
    params = {"robot_description": robot_description}

    pool_file = os.path.join(rov_gazebo_path, "description", "pool.xacro")
    pool_description = Command(["xacro ", pool_file])
    pool_params = {"robot_description": pool_description}

    # Create a robot_state_publisher node
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
        namespace=NS,
    )

    pool_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[pool_params],
        namespace=NS,
        remappings=[(f"/{NS}/robot_description", f"/{NS}/pool_description")],
    )

    # Launches Gazebo
    gazeboLaunch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(ros_ign_gazebo_path, "launch", "ign_gazebo.launch.py")]
        ),
        launch_arguments={"ign_args": world_path}.items(),
    )

    # Spawn entity
    ignition_spawn_entity = Node(
        package="ros_ign_gazebo",
        executable="create",
        output="screen",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "ROV",
            "-allow_renaming",
            "true",
        ],
        namespace=NS,
    )

    ignition_spawn_pool = Node(
        package="ros_ign_gazebo",
        executable="create",
        output="screen",
        arguments=[
            "-topic",
            "pool_description",
            "-name",
            "pool",
            "-allow_renaming",
            "true",
        ],
        namespace=NS,
    )

    # Not using keyboard launch file
    keyboard_driver = Node(
        package="keyboard_driver",
        executable="keyboard_driver_node",
        output="screen",
        name="keyboard_driver_node",
        namespace=NS,
        remappings=[(f"/{NS}/manual_control", "/manual_control")],
    )

    # Thrust Bridge
    thrust_bridge = Node(
        package="ros_ign_bridge",
        executable="parameter_bridge",
        namespace=NS,
        name="thrust_bridge",
        arguments=[
            "/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_front_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_back_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_back_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_front_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_front_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_back_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_back_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
        ],
        remappings=[
            (
                "/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_top_front_right_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_top_front_right_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_top_back_left_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_top_back_left_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_top_back_right_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_top_back_right_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_bottom_front_left_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_bottom_front_left_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_bottom_front_right_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_bottom_front_right_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_bottom_back_left_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_bottom_back_left_body_blade_joint/cmd_thrust",
            ),
            (
                "/model/rov/joint/thruster_bottom_back_right_body_blade_joint/cmd_thrust",
                f"/{NS}/model/rov/joint/thruster_bottom_back_right_body_blade_joint/cmd_thrust",
            ),
        ],
        output="screen",
    )

    cam_bridge = Node(
        package="ros_ign_bridge",
        executable="parameter_bridge",
        namespace=NS,
        name="cam_bridge",
        arguments=[
            "/bottom_cam/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image",
            "/bottom_cam/camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo",
            "/front_cam/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image",
            "/front_cam/camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo",
            "/manip_cam/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image",
            "/depth_cam@sensor_msgs/msg/Image@ignition.msgs.Image",
            "/depth_cam/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked",
        ],
        remappings=[
            (f"/{NS}/bottom_cam/image_raw", "/bottom_cam/image_raw"),
            (f"/{NS}/bottom_cam/camera_info", "/bottom_cam/camera_info"),
            (f"/{NS}/front_cam/image_raw", "/front_cam/image_raw"),
            (f"/{NS}/front_cam/camera_info", "/front_cam/camera_info"),
            (f"/{NS}/manip_cam/image_raw", "/manip_cam/image_raw"),
            (f"/{NS}/depth_cam", "/depth_cam/image_raw"),
            (f"/{NS}/depth_cam/points", "/depth_cam/points"),
        ],
        output="screen",
    )

    pos_bridge = Node(
        package="ros_ign_bridge",
        executable="parameter_bridge",
        namespace=NS,
        name="pos_bridge",
        arguments=[
            "/world/rov_simulation/dynamic_pose/info@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V",
        ],
        remappings=[
            ("/world/rov_simulation/dynamic_pose/info", f"/{NS}/rov_pose"),
        ],
        output="screen",
    )

    thruster_controller = Node(
        package="rov_gazebo",
        executable="thruster_controller_node",
        output="screen",
        namespace=NS,
        remappings=[
            (f"/{NS}/manual_control", "/manual_control"),
            (f"/{NS}/armed", "/armed"),
        ],
    )

    # Launches Controller
    surface_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(surface_main_path, "launch", "surface_all_nodes_launch.py")]
        ),
    )

    return LaunchDescription(
        [
            robot_state_publisher,
            pool_state_publisher,
            gazeboLaunch,
            ignition_spawn_entity,
            ignition_spawn_pool,
            keyboard_driver,
            thrust_bridge,
            cam_bridge,
            pos_bridge,
            thruster_controller,
            surface_launch,
        ]
    )
