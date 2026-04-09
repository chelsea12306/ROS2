import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zqc/ros2_ws/src/portfolio/ROS2/topic/install/python_topic'
