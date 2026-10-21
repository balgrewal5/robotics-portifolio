# Week 19 — MoveIt 2 and Robotic Manipulation

## Overview

Studied the MoveIt 2 framework for robot arm motion planning, collision avoidance and autonomous manipulation using ROS 2.

## Key Learning

- Explored the architecture of MoveIt 2.
- Understood robot descriptions using URDF and SRDF.
- Reviewed inverse kinematics and joint-space planning.
- Studied motion planning with OMPL-based planners.
- Understood collision detection and planning scenes.
- Explored the use of MoveGroupInterface.
- Examined grasp planning and pick-and-place task sequences.

## Pick-and-Place Pipeline

1. Detect and estimate the pose of an object.
2. Transform the target pose into the robot's planning frame.
3. Generate a collision-aware approach trajectory.
4. Move the end effector into the grasp position.
5. Close the gripper and attach the object in the planning scene.
6. Plan and execute movement towards the placement target.
7. Release the object and retract the arm.

## Outcome

Developed an understanding of how perception, kinematics, motion planning and control combine to support autonomous manipulation.

This week focused on theory and workflow demonstrations. Practical application is reserved for the autonomous manipulation portfolio project.
