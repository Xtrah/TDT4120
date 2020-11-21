

class HeapList:
    def __init__(self, arr, heapsize):
        self.arr = arr
        self.heapsize = heapsize

    def __str__(self):
        return str(self.arr)

    def __getitem__(self, item):
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def addNone(self):
        self.arr = [None] + self.arr
        self.heapsize += 1

    def removeNone(self):
        self.arr = self.arr[1:]
        self.heapsize -= 1

    def addInFront(self, value):
        self.arr = [value] + self.arr
        self.heapsize += 1

    def reduceHeapSize(self):
        self.heapsize -= 1

    def getArr(self):
        return self.arr