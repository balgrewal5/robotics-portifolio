
"""
Robotics Roadmap 1 - Week 17
Motion Planning: A* Pathfinding

Finds the shortest collision-free path
through a 2D occupancy grid.
"""

import heapq

# 0 = free space, 1 = obstacle
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 5)


def heuristic(a, b):
    """Manhattan distance for four-direction movement."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    if any(
        not (0 <= r < rows and 0 <= c < cols)
        or grid[r][c] != 0
        for r, c in (start, goal)
    ):
        raise ValueError("Start or goal is invalid")

    open_set = [(heuristic(start, goal), 0, start)]
    came_from = {}
    g_score = {start: 0}
    visited = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current in visited:
            continue

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            return path[::-1]

        visited.add(current)

        for dr, dc in directions:
            neighbour = (
                current[0] + dr,
                current[1] + dc
            )

            r, c = neighbour

            if not (0 <= r < rows and 0 <= c < cols):
                continue

            if grid[r][c] == 1 or neighbour in visited:
                continue

            new_cost = cost + 1

            if new_cost < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = new_cost
                came_from[neighbour] = current

                priority = new_cost + heuristic(neighbour, goal)

                heapq.heappush(
                    open_set,
                    (priority, new_cost, neighbour)
                )

    return None


path = astar(grid, start, goal)

if path:
    print("Shortest path:", path)
    print("Path length:", len(path) - 1, "steps")

    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[0])):
            position = (r, c)

            if position == start:
                line += "S "
            elif position == goal:
                line += "G "
            elif position in path:
                line += "* "
            elif grid[r][c] == 1:
                line += "# "
            else:
                line += ". "

        print(line)
else:
    print("No valid path found")
