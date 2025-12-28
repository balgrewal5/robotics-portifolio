# PID Controlled Go-to-goal-behaviour in 2D

import numpy as np
import matplotlib.pyplot as plt

# Helper function to wrap angle to [-pi, pi]
def wrap_to_pi(angle):
    # Wrap angle to [-pi, pi] so turning error doesn't exceed 180 degrees
    return (angle + np.pi) % (2 * np.pi) - np.pi

class Robot2D:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x   
        self.y = y
        self.theta = theta  # Orientation in radians
        # Control inputs (we will set these each time step)
        self.v = 0.0      # Forward speed
        self.w = 0.0      # Angular speed

    def step(self, dt):
        # Update robot pose using kinematics
        self.x += self.v * np.cos(self.theta) * dt   # Cos(theta) projects forward speed in x direction
        self.y += self.v * np.sin(self.theta) * dt   # Sine(theta) projects forward speed in y direction
        self.theta += self.w * dt
        # Keep theta within [-pi, pi]
        self.theta = wrap_to_pi(self.theta)


# Simulation parameters
dt= 0.05  # Time step
T= 20.0   # Total simulation time
t= np.arange(0.0, T, dt) # Time array
#Goal position
goal_x, goal_y = 10.0, 5.0
# Create robot instance
robot = Robot2D()
# Data storage for plotting
xs= []
ys= []
thetas= []
# PID parameters
kp= 1.0    # Proportional gain
ki= 0.1    # Integral gain
kd= 0.3    # Derivative gain
# PID errors initialization
integral_error= 0.0  
prev_error= 0.0      

# Simulation loop
for _ in t:
    #log current pose
    xs.append(robot.x)
    ys.append(robot.y)
    thetas.append(robot.theta)
    # Vector from robot to goal/ Turning errors into vectors
    dx= goal_x - robot.x 
    dy= goal_y - robot.y
    # Distance to goal
    distance_error= np.sqrt (dx*dx + dy*dy)       #For P
    # Stop if close enough to goal
    if distance_error < 0.1:
        break
    integral_error += distance_error * dt                  #For I
    derivative_error= (distance_error - prev_error) / dt   #For D
   # Compute control commands
    v_cmd = (kp * distance_error) + (ki * integral_error) + (kd * derivative_error)  # Control output for forward speed v
    angle_to_goal= np.arctan2(dy, dx)                                                # Angle from robot to goal
    heading_error= wrap_to_pi(angle_to_goal - robot.theta)                           # Heading error
# Set control inputs
    robot.v = min(v_cmd, 1.5)  # Limit max speed
    robot.w = 2.0* heading_error
    # Update robot
    robot.step(dt)
    prev_error= distance_error

# Plotting
plt.figure()
plt.plot(xs, ys, label="robot path")
plt.scatter([goal_x], [goal_y], marker="x", label="goal")
plt.axis("equal")
plt.grid(True)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Go-to-goal in 2D")
plt.legend()
plt.show()