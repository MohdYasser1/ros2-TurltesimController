import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class ShapeNode(Node):

    def __init__(self):
        super().__init__('shape_node')
        self.publisher_ = self.create_publisher(Int32, 'shape', 10)

    def publish_shape(self, user_shape):
        user_input = self.get_parameter('input_value').value
        print(user_input)
        msg = Int32()
        msg.data = user_shape
        self.publisher_.publish(msg)

class DoneDrawing(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'done',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        global done
        done = True
        

def main(args=None):
    done = False
    rclpy.init(args=args)

    shape_node = ShapeNode()
    
    while rclpy.ok():
        try:
            user_shape = int(input("Choose a shape:\n 1. shape1\n 2. shape2\n 3. shape3\n"))
            while (user_shape < 1) or (user_shape >3):
                print("\nSelect a valid number\n")
                user_shape = int(input("Choose a shape:\n 1. shape1\n 2. shape2\n 3. shape3\n"))
            print("Drawing...")
            shape_node.publish_shape(user_shape)
            while done == False:
                True
            print("Done drawing!\n \n")
            done = False
        except ValueError:
            print("\nInvalid input. Please try again")
    
    shape_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()        