import matplotlib.pyplot as plt 

class Robot1D:                   #Class defines a new object: 1D robot
    def __init__(self, x, v, a):    #Constructor method that runs when we create a robot
        self.x=x                 #Stores robots position inside the object
        self.v=v                 #Stores robots velocity inside the object
        self.a=a                 #Stores robots acceleration inside the object
    def update( self,dt):        #Method to update the robot's position
        self.v= self.v + self.a*dt    #Update velocity based on acceleration and time step
        self.x =self.x + self.v*dt     #Update position based on velocity and time step

robot = Robot1D( x=0.0, v=0.0, a=1.0)   #Create a robot object with initial position 0.0 and velocity 1.0

dt= 0.1
num_steps= 50                    #Number of time steps to simulate 50 steps*0.1s=5 sceonds 

xs= []                          #List to store robot positions over time
ts= []                          #List to store time steps

t=0.0                           #Initial time
for step in range( num_steps):  #Loop over each time step
    xs.append( robot.x)
    ts.append( t)
    
    robot.update( dt)           #Update the robot's position
    t += dt                     #Increment time by dt
    
    print( "Logged points:", len(ts))                     #Print number of logged points
    print( "First x:", xs[0], "Last x:", xs[-1])          #Print first and last logged positions

plt.plot( ts, xs)               #Plot position vs time
plt.xlabel( "Time (s)")         #Label x-axis 
plt.ylabel( "Position x (m)")   #Label y-axis
plt.title( "Robot1D: constant velocity motion")  #Title of the plot
plt.grid()                      #Add grid to the plot
plt.show()                      #Display the plot
