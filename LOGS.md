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