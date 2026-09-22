from setuptools import find_packages, setup
import os
from glob import glob

package_name = "ros2_basics"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        # add launch files
        (
            os.path.join("share", package_name, "launch"),
            glob("launch/*.launch.py"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="root@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            # add nodes here
            "sensor_publisher = ros2_basics.sensor_publisher:main",
            "temperature_monitor = ros2_basics.temperature_monitor:main",
            "warning_client = ros2_basics.warning_client:main",
        ],
    },
)
