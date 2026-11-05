def detect_repeating_pattern(values):
    n = len(values)
    for size in range(1, n // 2 + 1):
        if n % size == 0 and values[:size] * (n // size) == values:
            return values[:size]
    return None

if __name__ == "__main__":
    values = input("Enter values separated by spaces: ").split()
    pattern = detect_repeating_pattern(values)
    print("Repeating pattern:", pattern if pattern else "No exact repeating pattern")
