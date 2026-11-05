graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
         "D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}

def dfs(graph, start):
    visited, order = set(), []
    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order

if __name__ == "__main__":
    print("DFS traversal:", " -> ".join(dfs(graph, "A")))
