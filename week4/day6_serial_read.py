
import serial
import time

PORT = "COM9"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)                                # let arduino reset

print("Reading distance data...")

while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        try:
            distance = float(line)
            print(distance)
        except ValueError:
            pass