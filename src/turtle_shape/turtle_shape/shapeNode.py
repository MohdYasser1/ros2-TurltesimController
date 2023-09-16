import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class ShapeNode(Node):

    def __init__(self):
        super().__init__('shape_node')
        self.publisher_ = self.create_publisher(Int32, 'shape', 10)

    def publish_shape(self, user_shape):
        msg = Int32()
        msg.data = user_shape
        self.publisher_.publish(msg)


class QuitPublisher(Node):

    def __init__(self):
        super().__init__('quit_publisher')
        self.publisher_ = self.create_publisher(String, 'quit', 10)

    def publish_quit(self):
        msg = String()
        msg.data = "Quit"
        self.publisher_.publish(msg)
        

def main(args=None):
    done = False
    rclpy.init(args=args)

    shape_node = ShapeNode()
    quit_publisher = QuitPublisher()

    while rclpy.ok():

        user_shape = input("Choose a shape by selecting the number:\n 1. Star\n 2. Rose\n 3. SnowFlake\n\n 4. Stop\n")

        if user_shape == 's':
            quit_publisher.publish_quit()
            

        if user_shape == '1' or user_shape == '2' or user_shape == '3' or user_shape == '4':
            shape_node.publish_shape(int(user_shape))

        else:
            print("\nSelect a valid number\n")

    rclpy.spin(shape_node)
    rclpy.spin(quit_publisher)

    shape_node.destroy_node()
    quit_publisher.destroy_node()
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()        