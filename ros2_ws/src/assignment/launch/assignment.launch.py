from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    offset_arg = DeclareLaunchArgument(
        "offset",
        default_value="1",
        description="Offset for the temperature processor.",
    )
    return LaunchDescription(
        [
            offset_arg,
            Node(
                package="assignment",
                executable="sensor",
                output="screen",
                remappings=[
                    ("/temperature/raw", "/temperature/raw"),
                ],
            ),
            Node(
                package="assignment",
                executable="processor",
                output="screen",
                parameters=[
                    {"offset": LaunchConfiguration("offset")},
                ],
                remappings=[
                    ("/temperature/raw", "/temperature/raw"),
                    ("/temperature/processed", "/temperature/processed"),
                ],
            ),
            Node(
                package="assignment",
                executable="monitor",
                output="screen",
                remappings=[
                    ("/temperature/processed", "/temperature/processed"),
                ],
            ),
        ]
    )
