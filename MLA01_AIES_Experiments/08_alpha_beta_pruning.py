def alpha_beta(node, alpha, beta, maximizing, tree):
    if isinstance(tree[node], (int, float)):
        return tree[node]
    if maximizing:
        value = float("-inf")
        for child in tree[node]:
            value = max(value, alpha_beta(child, alpha, beta, False, tree))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for child in tree[node]:
        value = min(value, alpha_beta(child, alpha, beta, True, tree))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value

if __name__ == "__main__":
    tree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
            "D": 3, "E": 5, "F": 2, "G": 9}
    print("Best value:", alpha_beta("A", float("-inf"), float("inf"), True, tree))
