PLANETS = {
    "mercury": (1, "terrestrial"), "venus": (2, "terrestrial"),
    "earth": (3, "terrestrial"), "mars": (4, "terrestrial"),
    "jupiter": (5, "gas giant"), "saturn": (6, "gas giant"),
    "uranus": (7, "ice giant"), "neptune": (8, "ice giant")
}

def planet_fact(name):
    fact = PLANETS.get(name.lower().strip())
    if not fact:
        return "Planet not found."
    return f"{name.title()} is planet #{fact[0]} from the Sun and is a {fact[1]}."

if __name__ == "__main__":
    print(planet_fact(input("Enter planet name: ")))
