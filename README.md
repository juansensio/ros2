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


## Resources

- https://docs.ros.org/en/jazzy