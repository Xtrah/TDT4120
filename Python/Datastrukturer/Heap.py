from HeapList import HeapList as HL

import random

def exchange(A, idx_A, idx_B):
    temp = A[idx_A]
    A[idx_A] = A[idx_B]
    A[idx_B] = temp
    return A

def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return (2 * i) + 1

def build_max_heap(A):  # O(n*lg(n))) produces a max-heap from an unordered array
    for i in range(A.heapsize//2, -1, -1):  # n/2
        A = max_heapify(A, i)
    return A

# Max heap property: A[parent(i)] >= A[i], largest element is the root
# Min heap property: A[parent(i)] <= A[i], smallest element is the root
# Height of a heap: θ(lg n)

def max_heapify(A, idx):  # O(lg n), helps maintain the max-heap property
    if A[0] is not None:
        A.addNone()
        idx += 1
    leftIdx = left(idx)
    rightIdx = right(idx)
    largest = idx
    if leftIdx < A.heapsize and A[leftIdx] > A[largest]: # if the left child is larger than its parent
        largest = leftIdx
    if rightIdx < A.heapsize and A[rightIdx] > A[largest]: # if the right child is the largest
        largest = rightIdx
    if largest != idx: # if the parent is not the largest
        A = exchange(A, idx, largest) # Exchange the parent with the largest element
        A = max_heapify(A, largest) # Check if the element should be placed lower down
    if A[0] is None:
        A.removeNone()
    return A


def heapsort(A):
    A = build_max_heap(A) # n lg(n)
    for i in range(len(A.getArr())-1,0,-1): # n
        A = exchange(A, 0, i)
        A.reduceHeapSize()
        A = max_heapify(A,0) # lg n
    return A

arr = [1,1,2,6,39]
heap = HL(arr, len(arr))
heap = build_max_heap(heap)
#print(heap)

for i in range(10):
    heap.addInFront(random.randint(-100,100))
    heap = max_heapify(heap,0)

#print(heap)

arr = [3,2,6,19,2,3,-1,-53,2,4,5.34,-123]
testHeap = HL(arr, len(arr))
print(heapsort(testHeap))

