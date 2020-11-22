import random

def exchange(A, idx_A, idx_B):
    temp = A[idx_A]
    A[idx_A] = A[idx_B]
    A[idx_B] = temp


def partition(A, start, end):
    pivot = A[end]
    i = start - 1  # Index of smaller elements
    for j in range(start, end):
        if A[j] < pivot:  # If the element is smaller than the pivot
            i += 1  # Increment index of smaller elements
            exchange(A, i, j)  # Exchange the element at i with the element that is smaller than the pivot
    exchange(A, i + 1, end)  # The pivot is placed after all the elements that are smaller than itself
    return i + 1  # Return the index of the pivot


# Partition will still use the last index as pivot, so exchange the
def randomized_partition(A, start, end):
    i = random.randint(start, end)
    exchange(A, end, i)
    return partition(A, start, end)



def randomized_select(A, start, end, i): # Returns the ith smallest element
    if start == end:
        return A[start]
    pivot = randomized_partition(A, start, end) # all elements to the left of the pivot are smaller than the pivot
    k = pivot-start+1 # Find the amount of elements in the lower subarray (+1)
    if i == k: # If the amount of elements in the lower subarray (+1) equals to i
        return A[pivot] # Return the pivot element
    elif i < k:
        return randomized_select(A, start, pivot-1, i) # search in the lower subarray
    return randomized_select(A, pivot + 1, end, i - k) # search in the upper subarray

print(randomized_select([100,200,300,400,500,-200], 0, 5, 1))

# TODO: Write select algorithm (explanation on page 224)