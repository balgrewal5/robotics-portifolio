
"""
Robotics Roadmap 1 - Week 20
Trajectory Generation and Jacobian Control

Demonstrates:
- Quintic joint-space trajectories
- Proportional tracking with velocity feedforward
- 2-DOF manipulator Jacobian
- End-effector velocity calculation

Simplified numerical simulation; no real robot.
"""

import math

# Robot link lengths (metres)
L1 = 0.15
L2 = 0.12

# Initial and target joint angles (radians)
q_start = [0.0, 0.0]
q_goal = [math.radians(45), math.radians(30)]

duration = 3.0
dt = 0.05
kp = 4.0


def trajectory(t):
    """Quintic trajectory with zero endpoint velocity/acceleration."""
    tau = min(max(t / duration, 0.0), 1.0)

    # Position and velocity scaling
    s = 10*tau**3 - 15*tau**4 + 6*tau**5
    ds = (30*tau**2 - 60*tau**3 + 30*tau**4) / duration

    q_ref = [
        a + (b - a) * s
        for a, b in zip(q_start, q_goal)
    ]

    dq_ref = [
        (b - a) * ds
        for a, b in zip(q_start, q_goal)
    ]

    return q_ref, dq_ref


def jacobian_velocity(q, dq):
    """Map joint velocities to Cartesian velocity."""
    q1, q2 = q
    dq1, dq2 = dq

    j11 = -L1*math.sin(q1) - L2*math.sin(q1 + q2)
    j12 = -L2*math.sin(q1 + q2)

    j21 = L1*math.cos(q1) + L2*math.cos(q1 + q2)
    j22 = L2*math.cos(q1 + q2)

    vx = j11*dq1 + j12*dq2
    vy = j21*dq1 + j22*dq2

    return vx, vy


# Simulated joint positions
q_actual = q_start.copy()

print("Time | Joint 1 | Joint 2 | Vx | Vy")

steps = round(duration / dt)

for step in range(steps + 1):
    t = step * dt

    q_ref, dq_ref = trajectory(t)

    # Proportional tracking with velocity feedforward
    dq_command = [
        v + kp * (target - actual)
        for v, target, actual in zip(
            dq_ref, q_ref, q_actual
        )
    ]

    # Predicted Cartesian velocity
    vx, vy = jacobian_velocity(q_actual, dq_command)

    if step % 10 == 0:
        print(
            f"{t:.2f} | "
            f"{math.degrees(q_actual[0]):.1f} | "
            f"{math.degrees(q_actual[1]):.1f} | "
            f"{vx:.3f} | {vy:.3f}"
        )

    # Idealised velocity-controlled joint model
    if step < steps:
        q_actual = [
            q + dq * dt
            for q, dq in zip(q_actual, dq_command)
        ]

print("\nFinal joint tracking errors (degrees):")
for target, actual in zip(q_goal, q_actual):
    print(round(math.degrees(target - actual), 4))
