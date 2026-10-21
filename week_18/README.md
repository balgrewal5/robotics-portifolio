# Week 18 — ROS 2 Navigation (Nav2)

## Overview

Studied the ROS 2 Navigation 2 (Nav2) framework and how autonomous mobile robots navigate environments using localisation, mapping, path planning and motion control.

## Key Learning

- Understood the architecture of the Nav2 navigation stack.
- Explored the roles of map_server, AMCL and lifecycle nodes.
- Studied global and local costmaps for obstacle representation.
- Examined global path planning and local trajectory control.
- Understood behaviour trees for coordinating navigation tasks.
- Reviewed the integration of TF, odometry and sensor data.
- Explored navigation goal execution through ROS 2 actions.

## Navigation Pipeline

1. Receive a target navigation pose.
2. Estimate robot position using localisation.
3. Generate a global path through the environment.
4. Calculate velocity commands using a controller.
5. Monitor obstacles and update the local plan.
6. Recover or replan when necessary.

## Outcome

Developed a conceptual understanding of Nav2's architecture and autonomous navigation workflow.

This week focused on conceptual demonstrations rather than a completed hands-on Nav2 implementation. Further practical integration is planned for dedicated ROS 2 training.
