import launch
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    node = launch_ros.actions.Node(
        package='edit_cpp_py_package_name',  
        executable='py_node.py' 
    )

    return LaunchDescription([
        node
    ])