"""
Week 1 Day 1
Python foundations for robotics
"""
# Numeric types
time= 5 # seconds
velocity= 1.2 # m/s
position= velocity*time

# text
robot_name= "Diffbot"

#Boolean
is_enabled= True

print("Position:", position)
print("Robot:", robot_name)
print("Enabled:", is_enabled)

print(type(time))
print(type(velocity))
print(type(robot_name))
print(type(is_enabled))

battery_voltage= 10.9

if battery_voltage > 12.0:
    print("Battery fyll")
elif battery_voltage > 11.0:
    print("Battery medium")
else:
    print("Battery low")

# Simulated control loop

dt= 0.1
position= 0.0
velocity= 1.0

for step in range(10):
    position= position + velocity * dt
    print("step=", step, "position=", position)

t=0
dt=0.2
while t<2.0:
    print("control loop at t=",t)
    t= t + dt

def update_position(x, v, dt):
    return x + v * dt

x= 0
v= 1.5
dt= 0.1

for i in range(10):
    x= update_position( x, v, dt)
    print ("x=",x)


# Sensor array
laser_ranges = [1.2, 0.9, 1.5, 0.7]

for r in laser_ranges:
    print("Range:", r)

# Robot state dictionary
robot_state = {
    "x": 0.0,
    "y": 1.2,
    "theta": 0.5
}

print(robot_state["x"])
print(robot_state["theta"])


def simulate_motion( x, v ,dt):
    while x <= 2.0:
        x = x + v * dt
        print("x=", x)

simulate_motion(0.0, 0.6, 0.1)
