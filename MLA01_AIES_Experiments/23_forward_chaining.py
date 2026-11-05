RULES = [
    ({"has_power", "power_light_on"}, "computer_has_power"),
    ({"computer_has_power", "monitor_connected"}, "display_may_work"),
    ({"computer_has_power", "boot_error"}, "possible_boot_problem")
]

def forward_chain(facts):
    facts = set(facts)
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in RULES:
            if conditions <= facts and conclusion not in facts:
                facts.add(conclusion)
                changed = True
    return facts

if __name__ == "__main__":
    facts = input("Enter facts separated by commas: ").lower().split(",")
    result = forward_chain(f.strip() for f in facts if f.strip())
    print("Known and inferred facts:", sorted(result))
