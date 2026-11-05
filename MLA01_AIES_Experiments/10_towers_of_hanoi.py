def hanoi(n, source, auxiliary, destination):
    if n == 0:
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    hanoi(n, "A", "B", "C")
