from collections import deque

def solve_water_jug(cap_a, cap_b, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        (a, b), actions = queue.popleft()
        if a == target or b == target:
            return actions, (a, b)
        transfers = min(a, cap_b - b)
        transfers_back = min(b, cap_a - a)
        options = [
            ((cap_a, b), "Fill jug A"), ((a, cap_b), "Fill jug B"),
            ((0, b), "Empty jug A"), ((a, 0), "Empty jug B"),
            ((a - transfers, b + transfers), "Pour A into B"),
            ((a + transfers_back, b - transfers_back), "Pour B into A")
        ]
        for state, action in options:
            if state not in visited:
                visited.add(state)
                queue.append((state, actions + [action]))
    return None, None

if __name__ == "__main__":
    actions, state = solve_water_jug(4, 3, 2)
    print("Actions:", actions)
    print("Final state:", state)
