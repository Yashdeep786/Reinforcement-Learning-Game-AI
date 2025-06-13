import random

class SignalAgent:
    def __init__(self):
        self.memory = {}

    def choose_action(self, state):
        if state in self.memory:
            return self.memory[state]
        return self._random_pattern()

    def learn(self, state, action, reward):
        if reward > 0:
            self.memory[state] = action

    def _random_pattern(self):
        return ''.join(random.choices(['🔴', '🟡', '🟢', '🔵'], k=3))
