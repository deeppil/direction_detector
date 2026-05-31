import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from tf_transformations import euler_from_quaternion
import math


class DirectionDetector(Node):

    def __init__(self):
        super().__init__('direction_detector')

        self.last_direction = "NORTH"

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.direction_publisher = self.create_publisher(
            String,
            '/direction',
            10
        )

    def odom_callback(self, msg):

        q = msg.pose.pose.orientation

        roll, pitch, yaw = euler_from_quaternion([
            q.x,
            q.y,
            q.z,
            q.w
        ])

        self.get_logger().info(
            f"yaw = {yaw:.2f} rad"
        )

        yaw_deg = math.degrees(yaw)

        if -45 <= yaw_deg < 45:
            direction = "NORTH"

        elif 45 <= yaw_deg < 135:
            direction = "WEST"

        elif yaw_deg >= 135 or yaw_deg < -135:
            direction = "SOUTH"

        else:
            direction = "EAST"

        if direction != self.last_direction:
            direction_msg = String()
            direction_msg.data = direction

            self.direction_publisher.publish(direction_msg)

            self.get_logger().info(f"direction = {direction}")

            self.last_direction = direction


def main(args=None):
    rclpy.init(args=args)

    node = DirectionDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
