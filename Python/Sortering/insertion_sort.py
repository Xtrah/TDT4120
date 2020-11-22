# Side 18 i boka
# in-place
# comparison sort
# stable
testList = [4,3,2,7,6,7,20,4,36]

def insertion_sort(unsorted):
    for i in range(1, len(unsorted)): # θ(n)
        key = unsorted[i]
        j = i-1
        while j >= 0 and key < unsorted[j]: # O(n) if it must go to the bottom of the list each iteration , Ω(1) if everything is sorted
            unsorted[j+1] = unsorted[j]
            j-=1
        unsorted[j+1] = key
    return unsorted

# result:
# O(n^2) worst case (if it has to go through the entire list for each iteration in line 10)
# Best case: θ(n) (if the list is already sorted)


















## For repetition
def insertion_sort_2(unsorted):
    for i in range(1,len(unsorted)):
        key = unsorted[i]
        j = i-1
        while key < unsorted[j] and j >=0:
            unsorted[j+1] = unsorted[j]
            j-=1
        unsorted[j+1] = key
    return unsorted




print(testList)
print(insertion_sort_2(testList))