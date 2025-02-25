##################################################
##  Problem 3(c): Psyduck's Party Hats
##################################################

# Given n distinct integers in the range [0,N] where n <= N, find an integer
# in the range [0,N] that is missing. If there are multiple missing numbers,
# return any of them. There is at least one number in the range that is missing.
def find_missing_hat(A, N):
    '''
    Inputs:
        A       (list(int)) | List of unsorted, unique non-negative integers
        N       (int)       | A positive integer at least as large as len(A)
    Output:
        -       (int)       | An integer in the range [0,N] not present in arr
    '''

    ##################
    # YOUR CODE HERE #
    ##################
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
