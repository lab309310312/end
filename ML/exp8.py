import numpy as np

q = np.zeros((3, 2))

reward = [[-1, 0], [-1, 10], [0, 10]]

for i in range(100):
    state = np.random.randint(0, 3)

    action = np.argmax(q[state])

    next_state = min(state + 1, 2)

    q[state, action] += 0.1 * (
        reward[state][action] + 0.9 * np.max(q[next_state]) - q[state, action]
    )

print("Q-Table:\n", q)