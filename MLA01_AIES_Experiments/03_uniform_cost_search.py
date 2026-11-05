import heapq

graph = {"A": [("B", 1), ("C", 4)], "B": [("D", 2), ("E", 5)],
         "C": [("D", 1)], "D": [("F", 3)], "E": [("F", 1)], "F": []}

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    best = {start: 0}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if cost != best.get(node):
            continue
        if node == goal:
            return cost, path
        for nxt, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, nxt, path + [nxt]))
    return None, None

if __name__ == "__main__":
    cost, path = ucs(graph, "A", "F")
    print("Least-cost path:", " -> ".join(path) if path else "Not found")
    print("Cost:", cost)
