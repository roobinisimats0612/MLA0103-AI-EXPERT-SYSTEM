def sum_to_n(n):
    if n < 0:
        raise ValueError("N must be non-negative.")
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: "))
        print("Sum from 1 to", n, "=", sum_to_n(n))
    except (ValueError, RecursionError):
        print("Enter a reasonable non-negative integer.")
