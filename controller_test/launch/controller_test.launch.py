from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([
        Node(
            package='controller_test',
            executable='controller_test_node',
            name='controller_test'
        ),
        Node(
            package='joy',
            executable='game_controller_node',
            name='game_controller_node'
        )
    ])
