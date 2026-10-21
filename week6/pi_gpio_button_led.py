
"""
Robotics Roadmap 1 - Week 6
Raspberry Pi GPIO Fundamentals

Control an LED using a push button.
Demonstrates digital input/output, internal
pull-up resistors and event-driven GPIO.
"""

from gpiozero import LED, Button
from signal import pause

# GPIO pins (BCM numbering)
led = LED(17)
button = Button(27, pull_up=True, bounce_time=0.05)

# Button connects GPIO 27 to GND when pressed.
# Internal pull-up keeps input HIGH otherwise.

def button_pressed():
    led.on()
    print("Button pressed - LED ON")

def button_released():
    led.off()
    print("Button released - LED OFF")

# Register event callbacks
button.when_pressed = button_pressed
button.when_released = button_released

print("GPIO system running. Press the button.")

# Keep program running
pause()
