import random

class ContextMonitor:
    def collect(self):
        return {
            "network": random.choice(["good", "bad"]),
            "battery": random.randint(10, 100),
            "privacy_level": random.choice(["low", "high"])
        }
