parents = {("John","Alice"), ("John","Bob"), ("Mary","Alice"),
           ("Mary","Bob"), ("Alice","Carol")}

def children_of(parent):
    return sorted(child for p, child in parents if p == parent)

def siblings(person):
    parent_names = {p for p, child in parents if child == person}
    result = {child for p in parent_names for child in children_of(p)}
    result.discard(person)
    return sorted(result)

if __name__ == "__main__":
    print("Children of John:", children_of("John"))
    print("Siblings of Alice:", siblings("Alice"))
    print("Is Alice parent of Carol?", ("Alice", "Carol") in parents)
