def score(strategy, budgets):
    U = budgets["U"]
    P = budgets["P"]
    E = budgets["E"]
    R = budgets["R"]

    weights = {
        "LOCAL": (1.0, 0.1, 0.8, 0.9),
        "CLOUD": (0.9, 0.9, 0.3, 0.6),
        "SPLIT": (0.95, 0.5, 0.5, 0.8)
    }

    w = weights.get(strategy, (1,1,1,1))
    return w[0]*U - w[1]*P - w[2]*(1-E) - w[3]*(1-R)
