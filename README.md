# ROS 2

Learning ROS 2.

## Installation

Using docker on  mac os.

```
make run # start the container
make bash # open a bash shell in the container
```

First time, run the following commands in the container to install demos and configure the environment:

```
apt update

apt install -y \
  ros-jazzy-demo-nodes-cpp \
  ros-jazzy-demo-nodes-py \
  python3-colcon-common-extensions

echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc

source /opt/ros/jazzy/setup.bash

ros2 --help
echo $ROS_DISTRO
```

In the future, installing ROS 2 Jazz on Ubuntu 24.04 LTS.

> Need to upgrade ubuntu server to 24.04 LTS from 22.04 LTS.

## First steps

- `ros2 pkg create` must be executed in `/root/ros2_ws/src`
- `--build-type` can be `ament_python` or `ament_cmake` (for python and c++ respectively)
- add scripts inside the folder with the same name as the package to be executed by the `ros2 run` command.
- update `setup.py` to include the nodes in `entry_points`.
- `colcon build` must be executed in `/root/ros2_ws`, and then `source install/setup.bash` to source the installed packages.

## Resources

- https://docs.ros.org/en/jazzy
- https://github.com/MOGI-ROS/Week-1-2-Introduction-to-ROS2