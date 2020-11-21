import random
# Complexity θ(d*(O(x))) where O(x) is the running time of the stable sort (in this case counting sort
# In this case θ(d*(O(n)))

# The sorting algorithm must be stable. Possible candidates:
# Counting sort, merge sort, insertion sort, bubble sort
# The following are NOT stable: Quicksort, heapsort, selection sort
def modified_counting_sort(A, B, idx): # A = Usortert liste. B = Liste hvor resultatet skal puttes. idx = indeksen som sorteringen skal basere seg på
    k = 10
    C = [0]*(k+1)
    for i in range(len(A)):
        index = int(str(A[i])[idx])
        C[index] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        index = int(str(A[i])[idx])
        B[C[index]-1] = A[i]
        C[index] -= 1
    return B


def radix_sort(A, d):
    for i in range(d-1, -1, -1):
        B = [0]*len(A)
        A = modified_counting_sort(A,B,i)
    return A

for i in range(1000):
    testList = []
    for j in range(10):
        testList.append(random.randint(10,99))
    print(radix_sort(testList, 2))

