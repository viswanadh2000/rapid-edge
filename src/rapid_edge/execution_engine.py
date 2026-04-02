from rapid_edge.scoring import score

class ExecutionEngine:
    STRATEGIES = ["LOCAL", "CLOUD", "SPLIT"]

    def select(self, budgets):
        best = None
        best_score = float("-inf")

        for s in self.STRATEGIES:
            sc = score(s, budgets)
            if sc > best_score:
                best_score = sc
                best = s

        return best
