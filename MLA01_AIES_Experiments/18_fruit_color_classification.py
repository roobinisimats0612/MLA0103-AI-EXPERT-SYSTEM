RULES = {
    "red": ["apple", "strawberry", "cherry"],
    "yellow": ["banana", "lemon"],
    "orange": ["orange", "papaya"],
    "purple": ["grape", "plum"],
    "green": ["lime", "green apple"]
}

def classify_fruit(color):
    return RULES.get(color.lower().strip(), [])

if __name__ == "__main__":
    color = input("Enter fruit color: ")
    fruits = classify_fruit(color)
    print("Possible fruits:", ", ".join(fruits) if fruits else "No rule for this color.")
