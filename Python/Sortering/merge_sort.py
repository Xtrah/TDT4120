import sys

# O(nlgn) best, average and worst case
# Comparison sort
# Stable
def merge(A, start, mid, end):
    leftArr = A[start:mid+1] + [sys.maxsize]
    rightArr = A[mid+1:end+1] + [sys.maxsize]
    k = start
    i = 0
    j = 0
    while k <= end:
        if leftArr[i] < rightArr[j]:
            A[k] = leftArr[i]
            i += 1
        else:
            A[k] = rightArr[j]
            j += 1
        k += 1

def merge_sort(A, start, end):
    if start < end:
        mid = (start+end)//2
        merge_sort(A,start,mid)
        merge_sort(A,mid+1,end)
        merge(A, start, mid, end)



## for repetition
def merge_sort_2(A, start, end):
    if start < end:
        mid = (start+end)//2
        merge_sort_2(A, start, mid)
        merge_sort_2(A, mid + 1, end)
        merge2(A, start, mid, end)

def merge2(A, start, mid, end):
    leftArr = A[start:mid+1] + [sys.maxsize]
    rightArr = A[mid+1:end+1] + [sys.maxsize]
    k = start
    i = 0
    j = 0
    while k <= end:
        if leftArr[i] < rightArr[j]:
            A[k] = leftArr[i]
            i += 1
        else:
            A[k] = rightArr[j]
            j += 1
        k += 1








testList = [3,2,1,5,2,5,7,2,234]
merge_sort_2(testList,0,len(testList)-1)

print(testList)