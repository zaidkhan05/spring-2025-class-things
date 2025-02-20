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
topological_order = dfs_topological_sort(graph2)
print("Topological Order:", topological_order)
