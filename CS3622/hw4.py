import heapq

def dijkstra(graph, start):
    # Priority queue for selecting the node with the smallest tentative distance
    priority_queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(previous_nodes, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()
    return path

# Define the graph as an adjacency list
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 5, 'E': 4},
    'C': {'B': 5, 'F': 4, 'G': 3},
    'D': {'A': 3, 'E': 5},
    'E': {'B': 4, 'D': 5, 'F': 2},
    'F': {'C': 4, 'E': 2, 'G': 1},
    'G': {'C': 3, 'F': 1}
}

# Run Dijkstra's algorithm from node 'F'
distances, previous_nodes = dijkstra(graph, 'F')

# Print shortest distances from F to all nodes
print("Shortest distances from F:")
for node, distance in distances.items():
    print(f"F -> {node}: {distance}")

# Print the shortest path to each node
print("\nShortest paths:")
for node in graph:
    if node != 'F':
        path = shortest_path(previous_nodes, 'F', node)
        print(f"Path to {node}: {' -> '.join(path)}")
