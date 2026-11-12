"""Python equivalent of the syllabus item that specifically requests Prolog.
This is not Prolog source code."""
import heapq

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": ["G"], "E": ["G"], "F": ["G"], "G": []}
h = {"A": 6, "B": 4, "C": 3, "D": 2, "E": 1, "F": 2, "G": 0}

def best_first(start, goal):
    frontier = [(h[start], start, [start])]
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
                heapq.heappush(frontier, (h[nxt], nxt, path + [nxt]))
    return None

if __name__ == "__main__":
    path = best_first("A", "G")
    print("Heuristic path:", " -> ".join(path) if path else "Not found")
    print("Note: the original experiment specifies Prolog.")
