graph = {}
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):
	if node not in visited:
		print(node, end=" ")
		visited.add(node)
		
		for neighbour in graph[node]:
			dfs(visited, graph, neighbour)

key = int(input("\nEnter the number of nodes in the graph:- "))
for i in range(key):
	node = input("\nEnter a node:- ")
	neighbours = input("\nEnter its neighbours with spaces:- ").split()
	graph[node] = neighbours

print("\nGraph:- ", graph)

start_node = input("\nEnter a starting node for DFS traversal:- ")
print(f"\nFollowing is the Depth-First Search (Starting from Node {start_node}):- ")
dfs(visited, graph, start_node)