from rapid_edge.context_monitor import ContextMonitor
from rapid_edge.budget_estimator import BudgetEstimator
from rapid_edge.execution_engine import ExecutionEngine

monitor = ContextMonitor()
estimator = BudgetEstimator()
engine = ExecutionEngine()


def run_cycle():
    state = monitor.collect()
    budgets = estimator.estimate(state)
    decision = engine.select(budgets)

    return {
        "state": state,
        "budgets": budgets,
        "decision": decision
    }

if __name__ == "__main__":
    for _ in range(5):
        print(run_cycle())
