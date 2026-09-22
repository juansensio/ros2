import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from rclpy.qos import QoSProfile, ReliabilityPolicy

from ros2_basics_interfaces.msg import Temperature


class Monitor(Node):
    def __init__(self):
        super().__init__("monitor")
        qos = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,  # if the publisher is not reliable, the subscriber will not receive the messages
        )
        self.subscription = self.create_subscription(
            Temperature,
            "/temperature/processed",
            self.temperature_callback,
            qos,
        )

    def temperature_callback(self, message):
        self.get_logger().info(f"Processed temperature: {message.temperature:.2f} °C")


def main(args=None):
    rclpy.init(args=args)
    node = Monitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
