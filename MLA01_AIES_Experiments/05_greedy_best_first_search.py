import heapq

graph = {"Arad": ["Sibiu", "Timisoara", "Zerind"],
         "Sibiu": ["Arad", "Fagaras", "Rimnicu Vilcea"],
         "Timisoara": ["Arad", "Lugoj"], "Zerind": ["Arad", "Oradea"],
         "Fagaras": ["Sibiu", "Bucharest"],
         "Rimnicu Vilcea": ["Sibiu", "Pitesti"], "Lugoj": ["Timisoara"],
         "Oradea": ["Zerind", "Sibiu"], "Pitesti": ["Rimnicu Vilcea", "Bucharest"],
         "Bucharest": []}
h = {"Arad": 366, "Sibiu": 253, "Timisoara": 329, "Zerind": 374,
     "Fagaras": 176, "Rimnicu Vilcea": 193, "Lugoj": 244,
     "Oradea": 380, "Pitesti": 100, "Bucharest": 0}

def greedy_search(graph, h, start, goal):
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
    path = greedy_search(graph, h, "Arad", "Bucharest")
    print("Greedy path:", " -> ".join(path) if path else "Not found")
