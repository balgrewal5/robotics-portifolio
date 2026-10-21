
"""
Robotics Roadmap 1 - Week 14
YOLOv8 Object Detection with ROS 2

Subscribes to a camera image topic, detects dogs
and publishes the detection centre and confidence.

Dependencies: rclpy, sensor_msgs, std_msgs,
cv_bridge, ultralytics, OpenCV.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO


class YOLODetector(Node):

    def __init__(self):
        super().__init__("yolo_detector")

        self.bridge = CvBridge()
        self.model = YOLO("yolov8n.pt")

        self.subscription = self.create_subscription(
            Image,
            "/image",
            self.image_callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            "/dog_detection",
            10
        )

        self.get_logger().info("YOLO detector started")

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(
            msg, desired_encoding="bgr8"
        )

        results = self.model(frame, verbose=False)[0]

        # Select highest-confidence dog detection
        best_detection = None
        best_confidence = 0.0

        for box in results.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if (
                self.model.names[class_id] == "dog"
                and confidence > best_confidence
            ):
                best_detection = box
                best_confidence = confidence

        detection_msg = String()

        if best_detection is not None:
            x1, y1, x2, y2 = (
                best_detection.xyxy[0].tolist()
            )

            centre_x = (x1 + x2) / 2
            normalized_x = centre_x / frame.shape[1]

            detection_msg.data = (
                f"dog_detected "
                f"centre_x={normalized_x:.3f} "
                f"confidence={best_confidence:.2f}"
            )
        else:
            detection_msg.data = "no_dog"

        self.publisher.publish(detection_msg)


def main():
    rclpy.init()
    node = YOLODetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
