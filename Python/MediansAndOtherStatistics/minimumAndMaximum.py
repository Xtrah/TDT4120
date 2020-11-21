def find_minimum(A):
    min = A[0]
    for i in range(1, len(A)):
        if A[i] < min:
            min = A[i]
    return min

def find_minimum_and_maximum(A): # 3 comparisons for 2 elements at a time
    min = A[0]
    max = A[0]
    for i in range(1, len(A), 2):
        if A[i] > A[i - 1]:
            if A[i] > max:
                max = A[i]
            if A[i - 1] < min:
                min = A[i - 1]
        else:
            if A[i] < min:
                min = A[i]
            if A[i - 1] > max:
                max = A[i - 1]
    return (min,max)

print(find_minimum_and_maximum([1,5,2,10,15,2,3]))