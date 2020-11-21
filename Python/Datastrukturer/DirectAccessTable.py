class Node:
    def __init__(self, key, satellite_data):
        self.key = key
        self.satellite_data = satellite_data

    def __str__(self):
        return str(self.key) + " : " + str(self.satellite_data)

class DirectAccessTable:

    def __init__(self):
        self.T = [None]*1000

    def direct_address_search(self, k):
        if len(self.T) > k:
            return self.T[k]
        return None

    def direct_address_insert(self, x):
        if len(self.T) < x.key:
            self.T = self.T + [None]*1000 # expand table
        self.T[x.key] = x

    def direct_address_delete(self, x):
        if len(self.T) < x.key:
            return
        self.T[x.key] = None

    def __str__(self):
        result = "PRINTING ["
        for node in range(len(self.T)):
            if node != None:
                result += str(self.T[node]) + ", "
            else:
                result += "None, "
        return result + "]"


a = Node(2, [1,5,3,2])
b = Node(3, [2,3,69])
c = Node(10, [69,420])

dat = DirectAccessTable()

dat.direct_address_insert(a)
dat.direct_address_insert(b)
print(str(dat))
dat.direct_address_insert(c)

print(dat.direct_address_search(b.key))
dat.direct_address_delete(b)
print(dat.direct_address_search(b.key))
print(str(dat))


