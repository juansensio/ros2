from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    warning_threshold_arg = DeclareLaunchArgument(
        "warning_threshold",
        default_value="30.0",
        description="Warning threshold for the temperature monitor.",
    )
    temperature_topic_arg = DeclareLaunchArgument(
        "temperature_topic",
        default_value="/temperature",
        description="The name of the temperature topic to use (for remapping).",
    )
    return LaunchDescription(
        [
            warning_threshold_arg,
            temperature_topic_arg,
            Node(
                package="ros2_basics",
                executable="sensor_publisher",
                output="screen",
                remappings=[
                    ("/temperature", LaunchConfiguration("temperature_topic")),
                ],
            ),
            Node(
                package="ros2_basics",
                executable="temperature_monitor",
                output="screen",
                parameters=[
                    {"warning_threshold": LaunchConfiguration("warning_threshold")},
                ],
                remappings=[
                    ("/temperature", LaunchConfiguration("temperature_topic")),
                ],
            ),
        ]
    )
