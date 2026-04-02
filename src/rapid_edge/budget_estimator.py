class BudgetEstimator:
    def estimate(self, state):
        reliability = 1.0 if state.get("network") == "good" else 0.5
        privacy = 0.9 if state.get("privacy_level") == "high" else 0.2
        energy = state.get("battery", 100) / 100.0
        utility = 0.8
        return {
            "R": reliability,
            "P": privacy,
            "E": energy,
            "U": utility
        }
