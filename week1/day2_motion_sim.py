import numpy as np
import matplotlib.pyplot as plt

#Simulation settings
dt= 0.1
t_end= 10.0
t= np.arange(0.0, t_end + dt, dt)

#Part A: constant velocity model
#x_(k+1)= x_k+v*dt 
x0= 0.0         #initial postion
v= 1.2          #constant velcoty m/s

x_vel= np.zeros_like(t)
x_vel[0]= x0
for k in range (len(t)-1):
    x_vel[k+1] = x_vel[k] + v*dt

#Part B: Constant acceleration model
#v_{k+1} = v_k + a*dt
x_acc= np.zeros_like(t)
v_acc= np.zeros_like(t)

x_acc[0]= 0.0   #initial position
v_acc[0]= 0.0   #initial velocity
a= 0.6          #constant acc m/s^2

for k in range( len(t)-1):
    #update position using current velocity
    x_acc[k+1]= x_acc[k] + v_acc[k] *dt
    #update velocity using constant acceleration
    v_acc[k+1]= v_acc[k] + a*dt

#Plot results
plt.figure()
plt.plot(t, x_vel, label="Constant velocity")
plt.plot(t, x_acc, label="Constant acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Motion Simulation")
plt.legend()
plt.grid(True)
plt.show()
