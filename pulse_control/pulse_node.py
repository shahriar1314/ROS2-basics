import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class PulseNode(Node):
    def __init__(self):
        super().__init__('pulse_node')
        self.publisher_ = self.create_publisher(Bool, 'pulse', 10)
        self.subscription = self.create_subscription(String, 'control', self.control_callback, 10)
        self.timer = None
        self.pulse_state = False

    def control_callback(self, msg):
        if msg.data == 'start':
            self.start_publishing()
        elif msg.data == 'stop':
            self.stop_publishing()

    def start_publishing(self):
        if self.timer is None:
            self.timer = self.create_timer(1.0, self.timer_callback)
            self.get_logger().info('Started publishing')

    def stop_publishing(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None
            self.get_logger().info('Stopped publishing')

    def timer_callback(self):
        msg = Bool()
        self.pulse_state = not self.pulse_state
        msg.data = self.pulse_state
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PulseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
