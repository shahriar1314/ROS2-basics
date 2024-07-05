import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk

class PulseUI(Node):
    def __init__(self):
        super().__init__('pulse_ui')
        self.publisher_ = self.create_publisher(String, 'control', 10)
        self.init_ui()

    def init_ui(self):
        self.root = tk.Tk()
        self.root.title('Pulse Control')

        self.start_button = tk.Button(self.root, text='Start', command=self.start_pulse)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text='Stop', command=self.stop_pulse)
        self.stop_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def start_pulse(self):
        msg = String()
        msg.data = 'start'
        self.publisher_.publish(msg)
        self.get_logger().info('Sent start command')

    def stop_pulse(self):
        msg = String()
        msg.data = 'stop'
        self.publisher_.publish(msg)
        self.get_logger().info('Sent stop command')

    def on_closing(self):
        self.get_logger().info('GUI shutting down')
        self.destroy_node()
        self.root.destroy()

def main(args=None):
    rclpy.init(args=args)
    node = PulseUI()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
