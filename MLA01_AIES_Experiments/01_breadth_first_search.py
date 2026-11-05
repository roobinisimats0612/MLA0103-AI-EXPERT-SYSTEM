from collections import deque

graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
         "D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    path = bfs_shortest_path(graph, "A", "F")
    print("Shortest path:", " -> ".join(path) if path else "No path found")
