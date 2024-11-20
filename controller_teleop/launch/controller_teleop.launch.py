import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    config = os.path.join(
        get_package_share_directory('controller_teleop'),
        'config',
        'params.yaml'
        )
    
    return LaunchDescription([
        Node(
            package='controller_teleop',
            executable='controller_teleop_node',
            name='controller_teleop_node',
            parameters=[config]
        ),
        Node(
            package='joy',
            executable='game_controller_node',
            name='game_controller_node'
        )
    ])
