import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from rclpy.qos import QoSProfile, ReliabilityPolicy

from ros2_basics_interfaces.msg import Temperature


class Processor(Node):
    def __init__(self):
        super().__init__("processor")
        qos = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,  # if the publisher is not reliable, the subscriber will not receive the messages
        )
        self.subscription = self.create_subscription(
            Temperature,
            "/temperature/raw",
            self.processing_callback,
            qos,
        )
        self.declare_parameter("offset", 1)
        self.publisher = self.create_publisher(
            Temperature,
            "/temperature/processed",
            qos,
        )

    def processing_callback(self, message):
        self.get_logger().info(f"Raw temperature: {message.temperature:.2f} °C")
        processed_message = Temperature()
        processed_message.sensor_id = message.sensor_id
        processed_message.timestamp = message.timestamp
        processed_message.temperature = (
            message.temperature + self.get_parameter("offset").value
        )
        self.get_logger().info(
            f"Processed temperature: {processed_message.temperature:.2f} °C"
        )


def main(args=None):
    rclpy.init(args=args)
    node = Processor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
