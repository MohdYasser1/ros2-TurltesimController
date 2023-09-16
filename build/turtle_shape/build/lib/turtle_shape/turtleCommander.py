import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class TurtleCommander(Node):

    def __init__(self):
        super().__init__('turtle_commander')
        self.subscription = self.create_subscription(
            Int32,
            'shape',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        global shape
        shape = msg.data
        print("Recived")

def main(args=None):
    rclpy.init(args=args)

    turtle_commander = TurtleCommander()

    rclpy.spin(turtle_commander)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_commander.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()