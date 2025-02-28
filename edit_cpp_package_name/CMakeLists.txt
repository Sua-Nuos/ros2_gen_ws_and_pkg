cmake_minimum_required(VERSION 3.5)
project(edit_cpp_package_name)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Include Cpp "include" directory
include_directories(include)

add_executable(edit_node_name src/edit_node_name.cpp)
ament_target_dependencies(edit_node_name rclcpp std_msgs)

install(TARGETS
  edit_node_name
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY 
  launch 
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
