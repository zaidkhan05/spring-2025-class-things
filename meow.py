def floydWarshall(graph):
    V = len(graph)
    arr = ["A", "B", "C", "D", "E"]
    # Add all vertices one by one to
    # the set of intermediate vertices.
    for k in range(V):

        # Pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination
            # for the above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of graph[i][j]

                if ((graph[i][j] == -1 or 
                    graph[i][j] > (graph[i][k] + graph[k][j]))
                    and (graph[k][j] != -1 and graph[i][k] != -1)):
                    graph[i][j] = graph[i][k] + graph[k][j]
        print("graph " + arr[k] + ":")
        for i in range(len(graph)):
            for j in range(len(graph)):
                print(graph[i][j], end=" ")
            print()
        print("==========")

# if __name__ == "__main__":
#     # graph = [
#     #     [0, 2, -1, 1, 8],
#     #     [6, 0, 3, 2, -1],
#     #     [-1, -1, 0, 4, -1],
#     #     [-1, -1, 2, 0, 3],
#     #     [3, -1, -1, -1, 0]
#     # ]


#     graph = [
#         [0,3],
#         [-5,0]
#     ]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place the key in its correct position
        print("Step", i, ":", arr)

# # Given list
# arr = ['E', 'X', 'A', 'M', 'P', 'L', 'E']

# # Apply insertion sort
# insertion_sort(arr)

# # Print sorted list
# print("Sorted list:", arr)



def log_base_2(n):
    count = 0
    while n > 1:
        n //= 2  # Integer division by 2
        count += 1
    return count

# Example usage
n = 100   
print("⌊log₂({})⌋ =".format(n), log_base_2(n))
