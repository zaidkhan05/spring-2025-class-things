

def sort(A, N):
    low, high = 0, N
    
    if len(A) < 1:
        return 0
    while low <= high:
        mid = (low + high) // 2
        left, right = 0, len(A) - 1
        while left <= right:
            if A[left] < mid:
                left += 1
            elif A[right] >= mid:
                right -= 1
            else:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        if left < mid:
            high = mid - 1
        else:
            low = mid + 1

    # print(low - 1)
    return low - 1