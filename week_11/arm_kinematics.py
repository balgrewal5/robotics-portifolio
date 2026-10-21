
"""
Robotics Roadmap 1 - Week 11
2-DOF Planar Robot Arm Kinematics

Demonstrates:
- Forward kinematics (FK)
- Inverse kinematics (IK)
- Elbow-up and elbow-down solutions
- Analytical Jacobian
"""

import math

# Robot link lengths (metres)
L1 = 0.15
L2 = 0.12


def forward_kinematics(q1, q2):
    """Calculate end-effector position from joint angles."""
    x = L1 * math.cos(q1) + L2 * math.cos(q1 + q2)
    y = L1 * math.sin(q1) + L2 * math.sin(q1 + q2)
    return x, y


def inverse_kinematics(x, y):
    """Calculate both IK solutions for a reachable target."""
    r2 = x**2 + y**2

    cos_q2 = (r2 - L1**2 - L2**2) / (2 * L1 * L2)

    if not -1 <= cos_q2 <= 1:
        raise ValueError("Target is outside the robot workspace")

    solutions = []

    for sign in [1, -1]:
        sin_q2 = sign * math.sqrt(max(0, 1 - cos_q2**2))

        q2 = math.atan2(sin_q2, cos_q2)

        q1 = math.atan2(y, x) - math.atan2(
            L2 * sin_q2,
            L1 + L2 * cos_q2
        )

        solutions.append((q1, q2))

    return solutions


def jacobian(q1, q2):
    """Calculate the 2x2 analytical Jacobian."""
    j11 = -L1 * math.sin(q1) - L2 * math.sin(q1 + q2)
    j12 = -L2 * math.sin(q1 + q2)

    j21 = L1 * math.cos(q1) + L2 * math.cos(q1 + q2)
    j22 = L2 * math.cos(q1 + q2)

    return [[j11, j12], [j21, j22]]


def main():
    # Desired end-effector target (metres)
    target_x = 0.18
    target_y = 0.12

    print(f"Target: ({target_x}, {target_y}) m")

    solutions = inverse_kinematics(target_x, target_y)

    for name, (q1, q2) in zip(
        ["Elbow-up", "Elbow-down"], solutions
    ):
        print(f"\n{name} solution:")

        print(f"q1 = {math.degrees(q1):.2f} deg")
        print(f"q2 = {math.degrees(q2):.2f} deg")

        # Verify IK using forward kinematics
        x, y = forward_kinematics(q1, q2)
        print(f"FK verification: ({x:.4f}, {y:.4f}) m")

        print("Jacobian:")
        for row in jacobian(q1, q2):
            print([round(value, 4) for value in row])


if __name__ == "__main__":
    main()
