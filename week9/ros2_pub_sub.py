
"""
Robotics Roadmap 1 - Week 9
ROS 2 Fundamentals: Publisher and Subscriber

Demonstrates:
- ROS 2 nodes
- Topic-based communication
- Publisher and subscriber callbacks
- Timers and spinning
"""

import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        super().__init__('roadmap_publisher')

        self.publisher = self.create_publisher(
            String, 'roadmap_chatter', 10
        )

        self.counter = 0
        self.timer = self.create_timer(
            1.0, self.timer_callback
        )

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS 2! Message {self.counter}'

        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')

        self.counter += 1


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('roadmap_subscriber')

        self.subscription = self.create_subscription(
            String,
            'roadmap_chatter',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received: {msg.data}'
        )


def main():
    rclpy.init()

    publisher = PublisherNode()
    subscriber = SubscriberNode()

    executor = SingleThreadedExecutor()
    executor.add_node(publisher)
    executor.add_node(subscriber)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
