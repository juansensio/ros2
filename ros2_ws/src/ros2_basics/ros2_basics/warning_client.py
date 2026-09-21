import sys

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class WarningClient(Node):
    def __init__(self):
        super().__init__("warning_client")
        self.client = self.create_client(
            SetBool,
            "/set_warnings_enabled",
        )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self, enabled):
        request = SetBool.Request()
        request.data = enabled
        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = WarningClient()
    enabled = sys.argv[1].lower() == "true"
    future = node.send_request(enabled)
    rclpy.spin_until_future_complete(node, future)
    response = future.result()
    node.get_logger().info(f'success={response.success}, message="{response.message}"')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
