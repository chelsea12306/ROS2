import espeakng
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from queue import Queue
import threading
import time


class SubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name},start!')
        self.novels_queue_ = Queue()
        self.novel_subscriber_ = self.create_subscription(String, 'novel1', self.novel_callback, 10)
        self.speach_thread_ = threading.Thread(target=self.speak_thread)
        self.speach_thread_.start()

    def novel_callback(self, msg):
        self.novels_queue_.put(msg.data)
    
    def speak_thread(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'en-gb'

        while rclpy.ok():
            if self.novels_queue_.qsize()>0:
                text = self.novels_queue_.get()
                self.get_logger().info(f'reading:{text}')
                speaker.say(text)
                speaker.wait()
            else:
                time.sleep(1)
        

def main():
    rclpy.init()
    node = SubNode('sub')
    rclpy.spin(node)
    rclpy.shutdown()