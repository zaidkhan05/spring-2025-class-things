import time

def dfs_topological_sort(graph):
    visited = set()  # To track visited nodes
    stack = []  # To store the topological order

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:  # Visit all adjacent nodes
            dfs(neighbor)
        stack.append(node)  # Push the node onto the stack after visiting all children

    # Perform DFS for each unvisited node
    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack to get the topological order

def topological_sort_kahn(graph):
    # Step 1: Compute in-degree for each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Step 2: Collect nodes with in-degree 0 into a stack
    stack = [node for node in in_degree if in_degree[node] == 0]
    sorted_order = []
    
    # Step 3: Process nodes using stack (LIFO order)
    while stack:
        node = stack.pop()  # Last-in, first-out
        sorted_order.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    # If we processed all nodes, return the sorted order
    if len(sorted_order) == len(graph):
        return sorted_order
    else:
        return "Cycle detected! No valid topological order."





# Define the graph using adjacency list
graph1 = {
    'a': ['b'],
    'b': ['g'],
    'c': ['d', 'e'],
    'd': ['b', 'g'],
    'e': ['h'],
    'f': ['a', 'b'],
    'g': ['f'],
    'h': ['c', 'd']
}


graph2 = {
    'a': ['f'],
    'b': ['a', 'd', 'f'],
    'c': ['h'],
    'd': ['c', 'h'],
    'e': ['c'],
    'f': ['g'],
    'g': ['b', 'd'],
    'h': ['e']
}





# Apply topological sorting
sortTime = time.perf_counter()
topological_ordera = dfs_topological_sort(graph1)
sortTime = time.perf_counter() - sortTime
print(f"DFS Time for graph a:{sortTime:.8f} seconds")
sortTime = time.perf_counter()
topological_orderb = dfs_topological_sort(graph2)
sortTime = time.perf_counter() - sortTime
print(f"DFS Time for graph a:{sortTime:.8f} seconds")

sortTime = time.perf_counter()
kahn_ordera = topological_sort_kahn(graph1)
sortTime = time.perf_counter() - sortTime
print(f"Kahns Time for graph a:{sortTime:.8f} seconds")
sortTime = time.perf_counter()
kahn_orderb = topological_sort_kahn(graph2)
sortTime = time.perf_counter() - sortTime
print(f"Kahns Time for graph a:{sortTime:.8f} seconds")

print("dfs Order for graph a:", topological_ordera)

print("dfs Order for graph b:", topological_orderb)

print("Kahns Algorithm Order for graph a:", kahn_ordera)

print("Kahns Algorithm Order for graph b:", kahn_orderb)
