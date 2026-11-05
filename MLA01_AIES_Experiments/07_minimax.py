def minimax(node, maximizing, tree):
    if isinstance(tree[node], (int, float)):
        return tree[node]
    values = [minimax(child, not maximizing, tree) for child in tree[node]]
    return max(values) if maximizing else min(values)

if __name__ == "__main__":
    tree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
            "D": 3, "E": 5, "F": 2, "G": 9}
    print("Best minimax value:", minimax("A", True, tree))
