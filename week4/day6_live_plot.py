import serial
import time
import matplotlib.pyplot as plt

PORT = "COM9"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

distances = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_ylim(0, 200)
ax.set_xlabel("Samples")
ax.set_ylabel("Distance (cm)")
ax.set_title("Live Ultrasonic Distance")

while True:
    try:
        raw = ser.readline().decode("utf-8").strip()
        if raw:
            d = float(raw)
            distances.append(d)

            if len(distances) > 50:
                distances.pop(0)

            line.set_xdata(range(len(distances)))
            line.set_ydata(distances)

            ax.relim()
            ax.autoscale_view()

            plt.pause(0.05)

    except KeyboardInterrupt:
        print("Stopped")
        break
