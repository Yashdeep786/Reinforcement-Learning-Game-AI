# env/signal_env.py


class SignalEnv:
    def __init__(self):
        print("Signal environment initialized.")

    def receive_input(self, signal):
        # This can be used to manage state transitions or preprocess signal
        return signal

    def evaluate_response(self, feedback):
        # Converts feedback into a numeric reward
        return 1 if feedback == "👍 Yes" else -1

