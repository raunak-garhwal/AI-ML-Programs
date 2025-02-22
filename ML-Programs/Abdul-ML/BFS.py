from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

def get_user_input():
    graph = {}
    print("Enter the graph as adjacency list (e.g., A: B C D). Type 'done' when finished:")
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        node, neighbors = entry.split(":")
        graph[node.strip()] = [neighbor.strip() for neighbor in neighbors.split()]

    start = input("Enter the start node: ").strip()
    goal = input("Enter the goal node: ").strip()

    return graph, start, goal

def main():
    graph, start, goal = get_user_input()

    print("\nGraph:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")

    print(f"\nStarting BFS from {start} to {goal}...")
    path = bfs(graph, start, goal)

    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
