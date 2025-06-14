import random

class SignalAgent:
    def __init__(self):
        self.memory = {}  # signal → response → reward

    def choose_action(self, signal):
        if signal in self.memory:
            return max(self.memory[signal], key=self.memory[signal].get)
        else:
            return random.choice(["🟥", "🟦", "🔺", "⬛", "🟨"])

    def learn(self, signal, response, reward):
        if signal not in self.memory:
            self.memory[signal] = {}
        if response not in self.memory[signal]:
            self.memory[signal][response] = 0

        self.memory[signal][response] += reward
