birds = {"sparrow", "pigeon", "eagle", "penguin", "ostrich"}
flightless = {"penguin", "ostrich"}

def can_fly(animal):
    animal = animal.lower().strip()
    if animal not in birds:
        return "Animal is not listed in the bird knowledge base."
    if animal in flightless:
        return f"{animal.title()} cannot fly (exception rule)."
    return f"{animal.title()} can fly (default bird rule)."

if __name__ == "__main__":
    for bird in ["sparrow", "eagle", "penguin", "ostrich"]:
        print(can_fly(bird))
