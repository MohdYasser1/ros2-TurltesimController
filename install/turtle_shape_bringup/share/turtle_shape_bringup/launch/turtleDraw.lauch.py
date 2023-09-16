from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtle_shape',
            executable='shapeNode'
        ),
        Node(
            package='turtle_shape',
            executable='turtleCommander'
        )
    ])