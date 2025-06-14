import random

class SignalAgent:
    def __init__(self):
        # Define vocabulary and possible agent responses
        self.vocab = {
            '🟥': 'danger',
            '🟦': 'safe',
            '🔺': 'move up',
            '⬛': 'stop',
            '🟨': 'caution'
        }

        self.actions = list(self.vocab.keys())  # Possible response emojis

    def respond_to_signal(self, signal):
        # ✅ Return a random emoji as a dummy response (for now)
        return random.choice(self.actions)

    def learn(self, state, action, reward, next_state):
        # 🔧 Placeholder for Q-learning logic (not used yet)
        print(f"Learning: state={state}, action={action}, reward={reward}, next_state={next_state}")

    def choose_action(self, state):
        # example logic
        return state  # Replace with proper logic later
