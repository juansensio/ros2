import random
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy

from ros2_basics_interfaces.msg import Temperature


class SensorPublisher(Node):
    def __init__(self):
        super().__init__("sensor_publisher")
        qos = QoSProfile(
            depth=10,
            # reliability=ReliabilityPolicy.BEST_EFFORT, # if the publisher has a different reliability policy, the subscriber will not receive the messages
            reliability=ReliabilityPolicy.RELIABLE,
        )
        self.publisher = self.create_publisher(
            Temperature,
            "/temperature",
            # 10,  # the “queue size” is 10. limits the amount of queued messages if a subscriber is not receiving them fast enough.
            qos,
        )
        self.timer = self.create_timer(
            1.0,
            self.publish_temperature,
        )

    def publish_temperature(self):
        message = Temperature()
        message.sensor_id = "sensor_1"
        message.timestamp = self.get_clock().now().to_msg()
        message.temperature = random.uniform(18.0, 30.0)
        self.publisher.publish(message)
        self.get_logger().info(f"Temperature: {message.temperature:.2f} °C")


def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
