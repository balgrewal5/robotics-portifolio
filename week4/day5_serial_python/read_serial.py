import serial
import time

ser = serial.Serial("COM9", 9600, timeout=1)
time.sleep(2)

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    if line:
        print(line)
