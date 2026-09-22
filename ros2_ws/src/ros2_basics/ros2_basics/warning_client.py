import sys

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

from ros2_basics_interfaces.srv import SetThreshold


class WarningClient(Node):
    def __init__(self):
        super().__init__("warning_client")
        self.client = self.create_client(
            SetBool,
            "/set_warnings_enabled",
        )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")
        self.threshold_client = self.create_client(
            SetThreshold,
            "/set_threshold",
        )
        while not self.threshold_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self, enabled):
        request = SetBool.Request()
        request.data = enabled
        return self.client.call_async(request)

    def send_threshold_request(self, threshold):
        request = SetThreshold.Request()
        request.threshold = threshold
        return self.threshold_client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = WarningClient()
    enabled = sys.argv[1].lower() == "true"
    threshold = float(sys.argv[2])
    future_enabled = node.send_request(enabled)
    future_threshold = node.send_threshold_request(threshold)
    rclpy.spin_until_future_complete(node, future_enabled)
    response_enabled = future_enabled.result()
    rclpy.spin_until_future_complete(node, future_threshold)
    response_threshold = future_threshold.result()
    node.get_logger().info(
        f'success={response_enabled.success}, message="{response_enabled.message}", threshold={response_threshold.threshold}'
    )
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
