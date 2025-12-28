# Robot 2D motion with control inputs

import numpy as np
import matplotlib.pyplot as plt

class Robot2D:
# Initialize robot state
    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
# Add update step
    def step (self, ax, ay, dt):       # step advances the robot one timestep
        self.vx = self.vx + ax * dt    # update velocity using acceleration
        self.vy = self.vy + ay * dt    # update velocity using acceleration

        self.x = self.x + self.vx * dt  # update position using velocity
        self.y = self.y + self.vy * dt  # update position using velocity

# Control parameters
x_target= 10.0  # target x position
y_target= 5.0   # target y position
kp= 0.5          # proportional gain

# Build the 2D simulation
dt= 0.1          # time step
T= 10.0          # total time
t= np.arange(0.0, T + dt, dt)  # time array

robot= Robot2D()  # create robot instance

xs= []  # list to store x positions
ys= []  # list to store y positions

# Simulation loop
for i in enumerate(t):
    error_x= x_target - robot.x  # compute x error
    error_y= y_target - robot.y  # compute y error
    
    ax = kp * error_x  # control acceleration in x
    ay = kp * error_y  # control acceleration in y

    robot.step (ax, ay, dt)  # update robot state

    xs.append(robot.x)  #Updates x position list
    ys.append(robot.y)  #Updates y position list

# Plot the trajectory
plt.plot(xs, ys, label="robot path")
plt.xlabel("x position")
plt.ylabel("y position")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()