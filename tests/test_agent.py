import unittest
from rl_agent import Agent

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()

    def test_generate_signal(self):
        signal = self.agent.generate_signal()
        self.assertIsNotNone(signal, "Agent should generate a signal")
        self.assertIsInstance(signal, (str, list), "Signal should be a string or list")

    def test_learn_method(self):
        try:
            self.agent.learn(reward=1)
        except Exception as e:
            self.fail(f"Agent learn method raised an exception: {e}")

    def test_agent_state_after_learning(self):
        initial_state = getattr(self.agent, "state", None)
        self.agent.learn(reward=1)
        updated_state = getattr(self.agent, "state", None)
        self.assertNotEqual(initial_state, updated_state, "Agent state should change after learning")

if __name__ == "__main__":
    unittest.main()
