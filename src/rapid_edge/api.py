def get_decision(monitor, engine):
    state = monitor.collect()
    decision = engine.decide(state)
    return {"state": state, "decision": decision}
