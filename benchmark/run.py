import random

class ContextMonitor:
    def get_state(self):
        return {
            "network": random.choice(["good", "bad"]),
            "battery": random.randint(10, 100),
            "privacy_level": random.choice(["low", "high"])
        }

class DecisionEngine:
    def decide(self, state):
        if state["privacy_level"] == "high":
            return "LOCAL"
        if state["network"] == "bad":
            return "LOCAL"
        if state["battery"] < 20:
            return "CLOUD"
        return "SPLIT"

def simulate():
    monitor = ContextMonitor()
    engine = DecisionEngine()

    for _ in range(10):
        state = monitor.get_state()
        decision = engine.decide(state)
        print("State:", state, "Decision:", decision)

if __name__ == "__main__":
    simulate()
