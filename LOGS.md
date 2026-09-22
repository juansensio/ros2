# Day 2

## Goals

- Implement custom message and service types: https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Single-Package-Define-And-Use-Interface.html, https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html
- Launching https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Creating-Launch-Files.html

```
   temperature.launch.py
            │
    LaunchDescription
      ┌────┴────┐
      ▼         ▼
publisher    monitor
```

- Recording and replaying data (really cool! can record sensor and the play with controls and only tempetrature monitor node running): https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html
- Actions: https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html

```
Topic   -> continuous flow of data
Service -> short request + response
Action  -> objective that takes time + feedback + result + cancellation
```

- QoS & Debugging

```
"Not receiving messages"
        ↓
Do the nodes exist?
        ↓
Is the topic correct?
        ↓
Is the message type correct?
        ↓
Is the QoS compatible?
        ↓
Is the callback / logic correct?
```   

- Assignment: created 3 nodes (sensor, processor, monitor) with 2 topics using custom message. Launched them in a single launch file with arguments. Recorded the data and played it back with only the monitor node running.

## Issues

- types: https://docs.ros.org/en/jazzy/Concepts/Basic/About-Interfaces.html
- remember to run `source install/setup.zsh` after `colcon build --symlink-install` to source the installed packages.
- can build only one package with `colcon build --symlink-install --packages-select <package>`.
- `message.timestamp = self.get_clock().now().to_msg()` to convert the timestamp to a message.
- updating parameters with `self.set_parameters([new_param])`.
- launch files are in `launch/` folder, and are executed with `ros2 launch <package> <launch_file>`.
- pass arguments to launch with `ros2 launch <package> <launch_file> <parameter_name>:=<parameter_value>`.
- list arguments with `ros2 launch <package> <launch_file> --show-args`.
- add launch files to `setup.py` with `glob("launch/*.launch.py")`.
- create `bag_files` folder to store the recorded bags.
- can pass multiple argument to `ros2 bag record` to record multiple topics.
- can pass `-o <bag_file_name>` to specify the bag file name.
- `ros2 topic info <topic_name> --verbose` to check the QoS policy.

# Day 1

## Basics

- installation of ROS 2
- creation of a package
- creation of a node with python
- creation of a parameters, and change them at runtime
- creation of a service, and call it from a client
- basice cli commands

```
sensor_publisher
      │
      │ TOPIC: /temperature
      ▼
temperature_monitor
      │
      ├── PARAMETER: warning_threshold
      │
      └── SERVICE: set_warnings_enabled
                       ▲
                       │ request / response
                 warning_client
```

## Issues

- `ros2 pkg create` must be executed in `/root/ros2_ws/src`
- `--build-type` can be `ament_python` or `ament_cmake` (for python and c++ respectively)
- add scripts inside the folder with the same name as the package to be executed by the `ros2 run` command.
- update `setup.py` to include the nodes in `entry_points`.
- `colcon build` must be executed in `/root/ros2_ws`, and then `source install/setup.bash` to source the installed packages.
- `colcon build --symlink-install` for faster build and avoid the need to source the installed packages (useful for development).
- execute with `ros2 run <package> <node>`
