import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_srvs.srv import SetBool


class TemperatureMonitor(Node):
    def __init__(self):
        super().__init__("temperature_monitor")
        self.subscription = self.create_subscription(
            Float32,
            "/temperature",
            self.temperature_callback,
            10,
        )
        self.declare_parameter("warning_threshold", 25.0)
        self.warnings_enabled = True
        self.warning_service = self.create_service(
            SetBool,
            "set_warnings_enabled",
            self.set_warnings_enabled_callback,
        )

    def temperature_callback(self, message):
        threshold = self.get_parameter("warning_threshold").value
        if self.warnings_enabled and message.data >= threshold:
            self.get_logger().warning(
                f"HIGH TEMPERATURE: {message.data:.2f} °C "
                f"(threshold: {threshold:.2f} °C)"
            )
        else:
            self.get_logger().info(f"Temperature: {message.data:.2f} °C")

    def set_warnings_enabled_callback(self, request, response):
        self.warnings_enabled = request.data
        response.success = True
        response.message = (
            "Warnings enabled" if self.warnings_enabled else "Warnings disabled"
        )
        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
