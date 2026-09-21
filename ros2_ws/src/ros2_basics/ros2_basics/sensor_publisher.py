import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorPublisher(Node):
    def __init__(self):
        super().__init__("sensor_publisher")
        self.publisher = self.create_publisher(
            Float32,
            "/temperature",
            10,
        )
        self.timer = self.create_timer(
            1.0,
            self.publish_temperature,
        )

    def publish_temperature(self):
        message = Float32()
        message.data = random.uniform(18.0, 30.0)
        self.publisher.publish(message)
        self.get_logger().info(f"Temperature: {message.data:.2f} °C")


def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
