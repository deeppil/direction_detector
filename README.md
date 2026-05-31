# direction_detector
A reusable ROS 2 node that converts robot orientation from nav_msgs/msg/Odometry into human-readable cardinal directions (North, South, East, West). Compatible with any robot publishing standard ROS odometry messages. This is the first ROS2 node I've written, call it a test run, hoping to move onto more complicated projects soon. 

Graph with turtlebot3:
<img width="841" height="479" alt="image" src="https://github.com/user-attachments/assets/65009cf5-ce6a-48d1-a0e9-1eaa3a4cd260" />

## Installation

```
cd ~/ros2_ws/src
git clone https://github.com/deeppil/direction_detector.git
```

```
cd ~/ros2_ws
colcon build --packages-select direction_detector
source install/setup.bash
```

## Usage

```ros2 run direction_detector direction_detector```

```ros2 topic echo /direction```

## How It Works

1. Subscribe to /odom
2. Extract quaternion orientation
3. Convert quaternion to yaw
4. Convert yaw to cardinal direction
5. Publish direction on /direction
