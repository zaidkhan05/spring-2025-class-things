##################################################
##  Problem 6(b) Find the MissingNo.
##################################################

# Given a list of positive integers and the starting integer s, return x such that x is the smallest value greater than
# or equal to s that's not present in the list
def find_first_missing_element(arr, s):
    '''
    Inputs:
        arr        (list(int)) | List of sorted, unique positive integer order id's
        s          (int)       | Positive integer
    Output:
        -          (int)       | The smallest integer greater than or equal to s that's not present in arr
    '''
    ##################
    # YOUR CODE HERE #
    ##################

    left_bound, right_bound = 0, len(arr) - 1
    missing = s

    while left_bound <= right_bound:
        mid_point = (left_bound + right_bound) // 2

        if arr[mid_point] < missing:
            left_bound = mid_point + 1
        elif (mid_point - arr[mid_point] - missing) and (arr[mid_point] == missing):
                left_bound = mid_point + 1
                missing += 1
                print(missing)
        else:
            right_bound = mid_point - 1
    return missing

    # pass
