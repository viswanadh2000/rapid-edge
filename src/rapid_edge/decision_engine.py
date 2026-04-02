class DecisionEngine:
    def decide(self, state):
        if state.get("privacy_level") == "high":
            return "LOCAL"
        if state.get("network") == "bad":
            return "LOCAL"
        if state.get("battery", 100) < 20:
            return "CLOUD"
        return "SPLIT"
