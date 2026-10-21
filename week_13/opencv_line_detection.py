
"""
Robotics Roadmap 1 - Week 13
OpenCV Fundamentals: Line Detection

Demonstrates grayscale conversion, thresholding,
contour detection, centroid calculation and
visual feedback for line-following robotics.
"""

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Unable to open camera")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect a dark line against a light background
    _, mask = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 500:
            moments = cv2.moments(largest)

            if moments["m00"] != 0:
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])

                # Horizontal error from image centre
                error = cx - width // 2

                cv2.circle(
                    frame, (cx, cy), 6, (0, 0, 255), -1
                )
                cv2.drawContours(
                    frame, [largest], -1, (0, 255, 0), 2
                )

                print(f"Line centre: {cx} | Error: {error}")

    cv2.line(
        frame,
        (width // 2, 0),
        (width // 2, height),
        (255, 0, 0), 2
    )

    cv2.imshow("Line Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
