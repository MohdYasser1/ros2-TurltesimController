import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import math

go = True


class TurtleCommander(Node):

    def __init__(self):
        super().__init__('turtle_commander')
        self.shape = 0

        self.subscription = self.create_subscription(Int32,'shape',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 1)
        timer_period = 0.07  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0


    def listener_callback(self, msg):
        self.shape = msg.data
        go = True



    def timer_callback(self):

        if self.shape > 0:     
            self.i += 5
        print (self.i)
        if self.i > 360:
            # Publish done drawing
            True
        self.publisher_.publish(self.draw())


    def draw(self):

        self.y = 0.0
        self.x = 0.0
        print(self.shape)
        if self.shape == 1 or self.shape == 2 or self.shape == 3:
            r = self.polar_equation(self.i)
            print(r)
            self.x, self.y = self.polar_to_cartesian(r, math.radians(self.i))

        cmd_vel = Twist()
        cmd_vel.linear.x = self.x
        cmd_vel.linear.y = self.y
        return cmd_vel
    
    def polar_to_cartesian(self, radius, angle):
        
        x = 2* radius * math.cos(angle)
        y = 2* radius * math.sin(angle) 

        if self.shape == 1:
            x = x * 3
            y = y * 3

        return x, y
    
    def polar_equation(self, angle):
        angle = math.radians(angle)
        if self.shape == 1:
            r = math.cos(5 * angle)
        elif self.shape == 2:
            r = math.cos(0.3 * angle)
        elif self.shape == 3:
            r = (math.sin(1.2 * angle)) ** 2 + (math.cos(6 * angle)) ** 3
        else:
            r = 0
        
        return r
     

     


def main(args=None):
    rclpy.init(args=args)

    turtle_commander = TurtleCommander()

    rclpy.spin(turtle_commander)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_commander.destroy_node()
    # equation_turtle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()