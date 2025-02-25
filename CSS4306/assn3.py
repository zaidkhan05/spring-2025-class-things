import networkx as nx

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
    'a': ['b', 'c'],
    'b': ['e', 'g'],
    'c': ['f'],
    'd': ['a', 'b', 'f', 'g'],
    'e': [],
    'f': [],
    'g': ['f', 'e']
}

graph2 = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d'],
    'd': ['g'],
    'e': ['a'],
    'f': ['e', 'b', 'c', 'g'],
    'g': ['e']
}



# Apply topological sorting
topological_ordera = dfs_topological_sort(graph1)
topological_orderb = dfs_topological_sort(graph2)

kahn_ordera = topological_sort_kahn(graph1)
kahn_orderb = topological_sort_kahn(graph2)

print("Topological Order for graph a:", topological_ordera)

print("Topological Order for graph b:", topological_orderb)

print("Kahn's Algorithm Order for graph a:", kahn_ordera)

print("Kahn's Algorithm Order for graph b:", kahn_orderb)
