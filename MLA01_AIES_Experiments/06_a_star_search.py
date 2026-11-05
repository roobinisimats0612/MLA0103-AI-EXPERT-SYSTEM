import heapq

graph = {"A": [("B", 1), ("C", 4)], "B": [("D", 2), ("E", 5)],
         "C": [("D", 1)], "D": [("F", 3)], "E": [("F", 1)], "F": []}
h = {"A": 5, "B": 4, "C": 4, "D": 3, "E": 1, "F": 0}

def a_star(graph, h, start, goal):
    frontier = [(h[start], 0, start, [start])]
    best_g = {start: 0}
    while frontier:
        _, cost, node, path = heapq.heappop(frontier)
        if cost != best_g.get(node):
            continue
        if node == goal:
            return cost, path
        for nxt, edge in graph.get(node, []):
            new_cost = cost + edge
            if new_cost < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_cost
                heapq.heappush(frontier, (new_cost + h[nxt], new_cost, nxt, path + [nxt]))
    return None, None

if __name__ == "__main__":
    cost, path = a_star(graph, h, "A", "F")
    print("A* path:", " -> ".join(path) if path else "Not found")
    print("Cost:", cost)
