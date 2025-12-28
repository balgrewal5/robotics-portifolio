# Portfolio Project 1- PID-Controlled Go-To-Goal Robot (2D)

## Overview
This week focuses on building intuition and practical skill in robot motion and control.
The work progresses from second-order dynamics in 1D to a full 2D go-to-goal controller with heading and PID-based distance control.

All simulations are implemented from scratch in Python using discrete-time integration.

---

## Learning Objectives
- Understand second-order motion and inertia
- Implement P, PD, and PID controllers
- Extend motion from 1D to 2D
- Model robot state using classes
- Build a discrete simulation loop
- Implement go-to-goal behavior with heading control
- Integrate PID control into a mobile robot system

---

## Robot Model

The robot is modeled as a unicycle-type system with state:

- Position: `(x, y)`
- Heading: `θ`
- Control inputs:
  - Linear velocity `v`
  - Angular velocity `ω`

Motion equations:
ẋ = v cos(θ)
ẏ = v sin(θ)
θ̇ = ω

Discrete integration is performed using Euler integration.

---

## Project Structure

| File | Description |
|-----|------------|
| `day_second_order.py` | 1D second-order motion with inertia and PID control |
| `day4_robot2d.py` | 2D robot class and simulation loop |
| `day6_go_to_goal.py` | Go-to-goal behavior using heading control |
| `day7_pid_go_to_goal.py` | Full PID-controlled go-to-goal system |

---

## Control Strategy

### Distance Control (PID)
The distance to the goal is controlled using a PID controller:

- **P**: Drives the robot toward the goal
- **I**: Eliminates steady-state error
- **D**: Improves damping and stability

### Heading Control
The robot heading is controlled using proportional control on angular error:

- Target heading is computed using `atan2`
- Angular error is wrapped to `[-π, π]`
- Angular velocity is proportional to heading error

---

## Simulation Loop

At each timestep:
1. Compute vector from robot to goal
2. Calculate distance and heading error
3. Compute control commands
4. Update robot state
5. Log data for plotting
6. Stop when goal tolerance is reached

---

## Results

- The robot smoothly converges to the target position
- No oscillation or instability observed
- Heading aligns naturally with the goal direction
- PID distance control ensures precise stopping

The final trajectory demonstrates stable closed-loop control in 2D.

---

## Key Takeaways
- PID control is essential for accurate convergence
- Separating robot physics from control logic improves clarity
- Discrete simulation mirrors real embedded control loops
- This structure directly extends to real robots and ROS systems

---

## Next Steps
- Integrate this controller with real sensors
- Apply the same logic on embedded hardware (Arduino)
- Extend to obstacle avoidance and trajectory tracking
