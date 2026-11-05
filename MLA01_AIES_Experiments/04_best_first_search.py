import heapq

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": ["G"], "E": ["G"], "F": ["G"], "G": []}
h = {"A": 6, "B": 4, "C": 3, "D": 2, "E": 1, "F": 2, "G": 0}

def best_first(graph, heuristic, start, goal):
    frontier = [(heuristic[start], start, [start])]
    visited = set()
    while frontier:
        _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for nxt in graph.get(node, []):
            if nxt not in visited:
                heapq.heappush(frontier, (heuristic[nxt], nxt, path + [nxt]))
    return None

if __name__ == "__main__":
    path = best_first(graph, h, "A", "G")
    print("Path:", " -> ".join(path) if path else "Not found")
