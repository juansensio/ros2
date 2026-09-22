from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="assignment",
                executable="sensor",
                output="screen",
            ),
            Node(
                package="assignment",
                executable="processor",
                output="screen",
            ),
            Node(
                package="assignment",
                executable="monitor",
                output="screen",
            ),
        ]
    )
