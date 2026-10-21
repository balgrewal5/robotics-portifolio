
"""
Robotics Roadmap 1 - Week 22
Reinforcement Learning: DQN Maze Navigation

Custom 5x6 Gymnasium maze environment.
Train a Deep Q-Network using Stable-Baselines3.
Evaluate against a random-action baseline.

Reconstructed educational implementation.
"""

import numpy as np
import gymnasium as gym
from gymnasium import spaces
from stable_baselines3 import DQN


class MazeEnv(gym.Env):
    """Grid-world environment with obstacles and a goal."""

    def __init__(self):
        super().__init__()

        # 0 = free space, 1 = obstacle
        self.maze = np.array([
            [0, 0, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

        self.rows, self.cols = self.maze.shape
        self.goal = (4, 5)
        self.start = (0, 0)
        self.max_steps = 60

        # Four actions: up, down, left, right
        self.action_space = spaces.Discrete(4)

        # Observation: current grid-cell index
        self.observation_space = spaces.Discrete(
            self.rows * self.cols
        )

        self.valid_starts = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
            if self.maze[r, c] == 0
            and (r, c) != self.goal
        ]

    def observation(self):
        return self.pos[0] * self.cols + self.pos[1]

    def distance(self, pos):
        return (
            abs(pos[0] - self.goal[0])
            + abs(pos[1] - self.goal[1])
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        if options and "start" in options:
            self.pos = tuple(options["start"])
            if self.pos not in self.valid_starts:
                raise ValueError("Invalid starting position")
        else:
            index = self.np_random.integers(
                len(self.valid_starts)
            )
            self.pos = self.valid_starts[index]

        self.steps = 0
        return self.observation(), {}

    def step(self, action):
        moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        old_distance = self.distance(self.pos)
        dr, dc = moves[int(action)]

        nr = self.pos[0] + dr
        nc = self.pos[1] + dc

        reward = -0.05

        if (
            0 <= nr < self.rows
            and 0 <= nc < self.cols
            and self.maze[nr, nc] == 0
        ):
            self.pos = (nr, nc)
        else:
            reward -= 0.35

        # Reward progress towards the goal
        new_distance = self.distance(self.pos)
        reward += 0.3 * (old_distance - new_distance)

        self.steps += 1

        terminated = self.pos == self.goal
        truncated = self.steps >= self.max_steps

        if terminated:
            reward += 10.0

        if truncated and not terminated:
            reward -= 1.0

        return (
            self.observation(),
            reward,
            terminated,
            truncated,
            {}
        )


def evaluate(model, env, episodes=100, random=False):
    successes = 0
    successful_steps = []

    for i in range(episodes):
        start = env.valid_starts[i % len(env.valid_starts)]
        obs, _ = env.reset(options={"start": start})

        for step in range(env.max_steps):
            if random:
                action = env.action_space.sample()
            else:
                action, _ = model.predict(
                    obs, deterministic=True
                )

            obs, reward, done, truncated, _ = env.step(action)

            if done:
                successes += 1
                successful_steps.append(step + 1)

            if done or truncated:
                break

    rate = successes / episodes * 100
    avg_steps = (
        np.mean(successful_steps)
        if successful_steps else 0
    )

    return rate, avg_steps


def main():
    env = MazeEnv()

    print("Training DQN agent...")

    model = DQN(
        "MlpPolicy",
        env,
        learning_rate=0.001,
        buffer_size=10000,
        learning_starts=200,
        batch_size=64,
        gamma=0.99,
        train_freq=4,
        target_update_interval=250,
        exploration_fraction=0.5,
        exploration_final_eps=0.05,
        seed=42,
        verbose=0
    )

    # Train reinforcement learning agent
    model.learn(total_timesteps=10000)

    # Save trained model
    model.save("maze_dqn_model")

    # Compare random and trained policies
    random_rate, _ = evaluate(
        model, env, episodes=100, random=True
    )

    trained_rate, avg_steps = evaluate(
        model,
        env,
        episodes=len(env.valid_starts)
    )

    print("\n--- Evaluation Results ---")
    print(f"Random success rate: {random_rate:.1f}%")
    print(f"Trained success rate: {trained_rate:.1f}%")
    print(f"Average successful steps: {avg_steps:.1f}")

    # Evaluate fixed entrance-to-goal route
    obs, _ = env.reset(options={"start": (0, 0)})
    route = [env.pos]
    total_reward = 0.0

    for _ in range(env.max_steps):
        action, _ = model.predict(
            obs, deterministic=True
        )

        obs, reward, done, truncated, _ = env.step(action)

        total_reward += reward
        route.append(env.pos)

        if done or truncated:
            break

    print("\n--- Learned Route ---")
    print("Route:", route)
    print("Steps:", len(route) - 1)
    print("Total reward:", round(total_reward, 2))
    print("Reached goal:", env.pos == env.goal)

    env.close()


if __name__ == "__main__":
    main()
