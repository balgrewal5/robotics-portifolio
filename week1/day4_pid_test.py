# PID in a simple 1D simulation

import numpy as np                # for time arrays
import matplotlib.pyplot as plt   # to see visual results
from pid import PID               # import the PID controller class pid.py

pid= PID( kp=1.0, ki=0.1, kd=0.05)  # create a PID controller with chosen gains

target= 10.0                      # Where the robot should go
position= 0.0                     # Where the robot currently is 

# Time settings
dt= 0.1                         # How often the controller updates
t= np.arange(0.0, 10.0, dt)    # time array from 0-10s storign all dt, simulation runs every 10s, updates every 0.1s

# Storage of results for plotting
positions= []                   # To see how position changes over time
errors= []                      # To inspect error at each timestep  
controls= []                    # To inspect control effort

# Simulation loop/ Control loop
for _ in t:                        # For each time in the time array/ _means dont care about the value just count
      error= target - position     # +ve error means robot is behind, ive error means robot is overshooting
      u= pid.update( error, dt)    # Update the PID controller with current error & dt, get control signal u/ how hard to push

      position= position + u*dt    # Simple robot model: new position = old position + control signal(velocity) * dt

      positions.append( position)  # Store current position for plotting later
      errors.append( error)        # Store current error for plotting later
      controls.append(u)           # Store current control effort for plotting later
   
# Plotting results  
plt.plot(t, positions, label="position")
plt.plot(t, [target]*len(t), "--", label="target")
plt.xlabel("time (s)")
plt.ylabel("position")
plt.legend()
plt.grid(True)
plt.show()





