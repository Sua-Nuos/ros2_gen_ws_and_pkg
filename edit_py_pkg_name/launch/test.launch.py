import launch
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    node = launch_ros.actions.Node(
        package='edit_py_pkg_name',  
        executable='edit_node_name' 
    )

    return LaunchDescription([
        node
    ])