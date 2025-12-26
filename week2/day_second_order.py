#Week 2 Day 1: second-order motion

import numpy as np  
import matplotlib.pyplot as plt

# Initial conditions
x= 0.0
v= 0.0
# Simulation parameters
T= 5.0  # total simulation time
dt= 0.1  # time step

t= np.arange(0.0, T+ dt, dt)   # time array/ list of time instants we will iterate over

# Control parameters
x_target= 10.0 # target position
kp= 5.0 # proportional gain
kd= 2.0 # derivative gain
ki= 0.1 # integral gain
i_error= 0.0  # integral of error initialized to zero

# Logs (not used in this simple example, but useful for more complex simulations)
x_log= []  # list to log position over time (not used in this simple example)
v_log= []  # list to log velocity over time (not used in this simple example)
a_log= []  # list to log acceleration over time (not used in this simple example)


for _ in t:            # for each time instant in the time array t
    # Compute error
    error= x_target - x   # difference between target position and current position
    d_error= -v          # derivative of error is negative velocity
    i_error += error * dt  # integral of error/ += means accumulates over time

    # Compute acceleration using proportional control
    a= kp * error + kd * d_error + ki * i_error  # acceleration is proportional to the error, derivative of error, and integral of error
    

    # Update velocity and position using Euler integration
    v += a * dt     # update velocity based on acceleration
    x += v * dt     # update position based on velocity

    # Append current state to logs
    x_log.append(x)
    v_log.append(v)
    a_log.append(a)
   
print("Final x:", round(x, 3), "Final v:", round(v, 3))
plt.plot(t, x_log, label="x (position)")
plt.axhline(x_target, linestyle="--", label="target")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.grid(True)
plt.legend()
plt.show()


