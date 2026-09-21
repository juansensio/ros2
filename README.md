# ROS 2

Learning ROS 2.

## Installation

Using docker on  mac os.

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