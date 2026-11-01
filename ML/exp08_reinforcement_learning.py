"""
Experiment 8: Reinforcement Learning - Q-Learning on a Grid World
Environment is created inside the program (no external library needed).
 S . . .      S = start (0,0)   G = goal (+10)   X = pit (-10)   # = wall
 . # . X      every step costs -0.1
 . . . .
 . X . G
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)
rng = np.random.default_rng(0)

class GridWorld:
    ACTIONS = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}   # up, down, left, right
    ARROWS = ["^", "v", "<", ">"]

    def __init__(self):
        self.rows, self.cols = 4, 4
        self.start, self.goal = (0, 0), (3, 3)
        self.pits = {(1, 3), (3, 1)}
        self.walls = {(1, 1)}
        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, a):
        dr, dc = self.ACTIONS[a]
        r, c = self.state[0] + dr, self.state[1] + dc
        if 0 <= r < self.rows and 0 <= c < self.cols and (r, c) not in self.walls:
            self.state = (r, c)
        if self.state == self.goal:  return self.state, 10, True
        if self.state in self.pits:  return self.state, -10, True
        return self.state, -0.1, False

env = GridWorld()
Q = np.zeros((env.rows, env.cols, 4))
alpha, gamma = 0.1, 0.95
eps, eps_min, eps_decay = 1.0, 0.05, 0.995
episodes, max_steps = 2000, 100
rewards = []

for ep in range(episodes):
    s = env.reset(); total = 0
    for _ in range(max_steps):
        a = rng.integers(4) if rng.random() < eps else int(np.argmax(Q[s]))      # epsilon-greedy
        s2, r, done = env.step(a)
        Q[s][a] += alpha * (r + gamma * np.max(Q[s2]) * (not done) - Q[s][a])      # Bellman update
        s, total = s2, total + r
        if done: break
    eps = max(eps_min, eps * eps_decay)
    rewards.append(total)
    if (ep + 1) % 400 == 0:
        print(f"Episode {ep+1:4d} | avg reward (last 100) = {np.mean(rewards[-100:]):6.2f} | epsilon = {eps:.3f}")

# ---- Learned policy ----
print("\nLearned policy (greedy):")
for r in range(env.rows):
    row = ""
    for c in range(env.cols):
        if (r, c) == env.goal: row += " G "
        elif (r, c) in env.pits: row += " X "
        elif (r, c) in env.walls: row += " # "
        else: row += f" {env.ARROWS[int(np.argmax(Q[r, c]))]} "
    print(row)

# ---- Run greedy policy ----
s = env.reset(); path = [s]
for _ in range(20):
    s, r, done = env.step(int(np.argmax(Q[s]))); path.append(s)
    if done: break
print("\nGreedy path:", path)

w = 50
smooth = np.convolve(rewards, np.ones(w) / w, mode="valid")
plt.plot(smooth); plt.xlabel("Episode"); plt.ylabel(f"Reward (moving avg {w})"); plt.title("Q-Learning training curve")
plt.savefig("output/exp8_rewards.png", dpi=120); plt.close()
plt.imshow(Q.max(axis=2), cmap="viridis"); plt.colorbar(label="max Q"); plt.title("State values")
plt.savefig("output/exp8_values.png", dpi=120); plt.close()
