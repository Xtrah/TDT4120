class Node:
    def __init__(self, key):
        self.prev = None
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)

class LDoubly:
    def __init__(self):
        self.head = None

    def list_search(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def list_insert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def list_delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def list_print(self):
        x = self.head
        print("\n[x.prev, x.key, x.next]:")
        while x != None:
            print("Node: [" + str(x.prev) + "," + str(x.key) + "," + str(x.next) + "], ")
            x = x.next

class LSingly:
    def __init__(self):
        self.head = None

    def list_length(self):
        x = self.head
        if x == None:
            return 0
        i = 1
        while x.next != None:
            x = x.next
            i += 1
        return i

    def list_search(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def list_insert(self,x):
        x.next = self.head
        self.head = x

    def list_delete(self, x):
        y = self.head
        if (self.head == x):
            self.head = x.next
            return
        while y.next != x and y.next != None:
            y = y.next
        if y.next != None:
            y.next = x.next
            return
        print("The node that you wish to delete doesn't exist")


    def list_print(self):
        x = self.head
        print("\n[x.key, x.next]:")
        while x != None:
            print("Node: [" + str(x.key) + "," + str(x.next) + "], ")
            x = x.next

    def __str__(self):
        result = "["
        x = self.head
        while x != None:
            result += str(x.key) + ","
            x = x.next
        return result + "]"

if False:
    ## Doubly linked
    L = LDoubly()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    L.list_insert(a)
    L.list_insert(b)
    L.list_insert(c)
    L.list_print()
    print(L.list_search(2))
    L.list_delete(b)
    print(L.list_search(2))
    L.list_print()

    ## Singly linked
    L = LSingly()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    L.list_insert(a)
    L.list_insert(b)
    L.list_insert(c)
    L.list_print()
    print(L.list_search(1))
    L.list_delete(a)
    print(L.list_search(1))
    L.list_print()

