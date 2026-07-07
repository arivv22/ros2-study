#!/bin/bash

# Launch publisher and subscriber nodes
cleanup(){
    echo "Restarting ROS2 daemon"
    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "ROS2 daemon restarted"
    kill 0
    exit 
}

trap 'cleanup' SIGINT

# Launch Publisher node
ros2 run ros2_fundamentals_examples py_minimal_publisher.py &

sleep 2

# Launch Subscriber node
ros2 run ros2_fundamentals_examples py_minimal_subscirber.py
