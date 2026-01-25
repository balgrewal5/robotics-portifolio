# Week 4 — Arduino Foundations

## Day 1 — Digital I/O
Built a pushbutton input using `INPUT_PULLUP` and controlled an LED from a digital pin.

## Day 2 — PWM basics
Used PWM (`analogWrite`) to control output strength (duty cycle) and understood why it feels like “variable voltage”.

## Day 3 — Motor driver + PWM speed control
Wired a motor driver to Arduino and controlled motor speed with PWM while keeping a common ground.

## Day 4 — HC-SR04 ultrasonic distance
Measured distance using trigger/echo timing and verified stable readings in the Serial Monitor.

## Day 5 — Arduino ↔ Python serial
Read Arduino serial output in Python using `pyserial` and confirmed correct parsing of numeric data.

## Day 6 — Live plotting mini-project
Streamed ultrasonic distance to Python and plotted live measurements in real time.

## Notes
- Board: Arduino Uno R3
- Sensor: HC-SR04
- Key lesson: hardware + firmware + serial + Python must all agree (pins, baud rate, data format).
