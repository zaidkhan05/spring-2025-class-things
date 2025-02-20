def insertion_sort(A):
    # Iterate from the second element to the last
    for j in range(1, len(A)):
        print("\t", A)
        key = A[j]
        # Insert A[j] into the sorted sequence A[0..j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        

# Example usage
A = [31, 41, 59, 26, 41, 58]
insertion_sort(A)
print("\t", A)
