graph = {}
visited = []   # List for visited nodes.
queue = []     # Initialize a queue

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)

	while queue:   # Creating loop to visit each node
		m = queue.pop(0) 
		print(m, end=" ")

		for neighbour in graph[m]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
				
key = int(input("\nEnter the number of nodes in the graph:- "))
for i in range(key):
	node = input("\nEnter a node:- ")
	neighbours = input("\nEnter its neighbours with spaces:- ").split()
	graph[node] = neighbours

print("\nGraph:- ", graph)

start_node = input("\nEnter a starting node for BFS traversal:- ")
print(f"\nFollowing is the Breadth-First Search (Starting from Node {start_node}):- ")
bfs(visited, graph, start_node)