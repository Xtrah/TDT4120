import LinkedList as LL
import random
import math
class HashTable:

    def __init__(self):
        self.T = []
        for i in range(10):
            self.T.append(LL.LSingly())

    def hash_search(self, k):
        hashKey = self.hash_function(k)
        if hashKey > len(self.T):
            return None
        return self.T[hashKey].list_search(k)

    def hash_insert(self, x):
        hashKey = self.hash_function(x.key)
        while len(self.T) < hashKey+1: # TODO: Use Table-insert instead of this (p 464)
            self.T.append(LL.LSingly())
        self.T[hashKey].list_insert(x)

    def hash_delete(self, x):
        hashKey = self.hash_function(x.key)
        if len(self.T) < hashKey:
            return
        self.T[hashKey].list_delete(x)

    def hash_function(self, key): # TODO: Modify dis
        A = (math.sqrt(5) - 1)/2
        m = 2**5
        b = (key*A) % 1
        return math.floor(m*b)

    def __str__(self):
        result = "["
        for node in self.T:
            result += str(node) + ","
        result += "]\n Fordeling: ["
        for node in self.T:
            result += str(node.list_length()) + ","
        result += "]"
        return result



for i in range(3000): # reliability testing
    ht = HashTable()
    for j in range(1000):
        a = LL.Node(random.randint(0,100))
        ht.hash_insert(a)

    print("\n\n" + str(ht))

    ht.hash_delete(a)
