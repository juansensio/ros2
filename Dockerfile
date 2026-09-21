FROM ros:jazzy

WORKDIR /root/ros2_ws

RUN apt update && apt install -y \
    ros-jazzy-demo-nodes-cpp \
    ros-jazzy-demo-nodes-py \
    python3-colcon-common-extensions

RUN echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc