class SignalEnv:
    def __init__(self):
        self.state = None

    def receive_input(self, user_pattern):
        self.state = user_pattern
        return self.state

    def evaluate_response(self, user_feedback):
        return 1 if user_feedback == 'yes' else -1
