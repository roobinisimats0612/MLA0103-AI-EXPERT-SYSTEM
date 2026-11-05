from collections import deque

# State: (monkey position, box position, has banana)
POSITIONS = ("door", "middle", "window")

def successors(state):
    monkey, box, has_banana = state
    if has_banana:
        return []
    options = []
    for pos in POSITIONS:
        if pos != monkey:
            options.append(((pos, box, False), f"Walk to {pos}"))
    if monkey != box:
        options.append(((monkey, monkey, False), "Push box to current position"))
    if monkey == box == "middle":
        options.append(((monkey, box, True), "Climb box and grab banana"))
    return options

def solve():
    start = ("door", "window", False)
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, actions = queue.popleft()
        if state[2]:
            return actions
        for nxt, action in successors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, actions + [action]))
    return None

if __name__ == "__main__":
    plan = solve()
    print("Plan:")
    print("\n".join(f"{i}. {a}" for i, a in enumerate(plan or [], 1)) or "No plan found")
