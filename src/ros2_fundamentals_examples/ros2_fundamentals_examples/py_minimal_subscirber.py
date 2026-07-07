#! /usr/bin/env python3

""" summary
Description: Minimal subscriber example
---
Subscribing Topic: topic
Message Type: std_msgs/String
---- 
Publishing Topic: None

--- 
Subcription Topics:
   The channel containing the "Hello World" message
   /py_example_topic - stg_msgs/String

--- 
Author: Arief Malik
Date : Jul 07 2025
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10
        )
        # prevent unused variable warning
        self.subscription  
    
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    
    minimal_subscriber = MinimalSubscriber()
    
    rclpy.spin(minimal_subscriber)
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
