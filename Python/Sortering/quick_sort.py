import random


# θ(n^2) worst case - when the partitioning is entirely uneven T(n)=T(n-1)+T(0)+θ(n)
# θ(nlgn) average case - Constant split proportionality, e.g. T(n)=T(9n/10)+T(n/10)+θ(n)
# θ(nlgn) best case - Entirely even split, T(n)=2T(n/2)+θ(n)
# in place
# NOT stable
# comparison sort

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


def quicksort(A, start, end):
    if start < end:
        mid = randomized_partition(A, start, end)  # Put the pivot in the right place
        quicksort(A, start, mid - 1)
        quicksort(A, mid + 1, end)


for i in range(10000):
    tempList = []
    for j in range(5):
        tempList.append(random.randint(-10, 10))
    print(tempList)
    quicksort(tempList, 0, len(tempList) - 1)
    print(tempList)
    print("\n")
