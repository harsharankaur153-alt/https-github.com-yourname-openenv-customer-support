from models import Observation, Action
import random

class CustomerSupportEnv:
    def __init__(self):
        self.tasks = [
            {"query": "My order is delayed", "answer": "apology"},
            {"query": "I want refund", "answer": "refund"},
            {"query": "App is crashing", "answer": "technical"}
        ]
        self.current = None
        self.done = False

    def reset(self):
        self.current = random.choice(self.tasks)
        self.done = False
        return Observation(query=self.current["query"])

    def step(self, action: Action):
        expected = self.current["answer"]
        response = action.response.lower()

        reward = 0.0

        # incremental reward
        if expected in response:
            reward += 0.6
        if "sorry" in response:
            reward += 0.2
        if len(response) > 15:
            reward += 0.2

        self.done = True

        return Observation(query=self.current["query"]), reward, self.done, {}

    def state(self):
        return self.current