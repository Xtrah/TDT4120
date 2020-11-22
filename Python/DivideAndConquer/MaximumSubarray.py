import sys

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -sys.maxsize
    sum = 0
    max_left = -1
    for i in range(mid, low-1, -1): # important that you go "downto", because you need to know what comes AFTER idx i (we are finding the CROSS sum)
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -sys.maxsize
    sum = 0
    max_right = -1
    for i in range(mid+1, high+1): # Important the you go "upto" because you need to know what comes BEFORE idx i (we are finding the CROSS sum)
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A,low, high):
    if high == low: # If there is only one element left
        return (low,high,A[low]) # return it
    mid = (low + high) // 2
    (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid) # Find highest left sum
    (right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1, high) # Find highest right sum
    (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high) # Find highest cross sum
    if left_sum >= right_sum and left_sum >= cross_sum: # If left sum is highest, return it
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum: # If right sum is highest, return it
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum # If cross sum is highest, return it


testArray = [10,15,20,-5,30,-20,-10,-30,5,40]

print(find_maximum_subarray(testArray,0,len(testArray)-1)) # FUNKER :D


