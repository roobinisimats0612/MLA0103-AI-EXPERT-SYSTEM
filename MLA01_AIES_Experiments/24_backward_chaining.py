RULES = {
    "possible_cold": [{"sneezing", "runny_nose"}],
    "needs_checkup": [{"fever", "persistent_symptoms"}],
    "possible_respiratory_issue": [{"cough", "fever"}]
}

def prove(goal, facts, seen=None):
    if goal in facts:
        return True
    seen = set() if seen is None else seen
    if goal in seen:
        return False
    seen.add(goal)
    return any(all(prove(condition, facts, seen.copy()) for condition in rule)
               for rule in RULES.get(goal, []))

if __name__ == "__main__":
    facts = {x.strip().lower() for x in input("Known facts (comma-separated): ").split(",") if x.strip()}
    goal = input("Goal to prove: ").strip().lower()
    print("Goal proved:", prove(goal, facts))
    print("Educational demonstration only; not medical advice.")
