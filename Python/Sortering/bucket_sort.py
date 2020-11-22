import math

# Best case: θ(n)
# Average case: θ(n)
# Worst case: θ(n^2)

def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def bucket_sort(A):
    n = len(A)
    B = []
    for i in range(n):
        B.append([])
    for i in range(n):
        idx = math.floor(n*A[i])
        B[idx].append(A[i])
    for i in range(n):
        B[i] = insertion_sort(B[i])
    return sum(B, []) # Concatenate all lists


testList = [0.1, 0.2, 0.15, 0.5, 0.23, 0.142]
print(bucket_sort(testList))

