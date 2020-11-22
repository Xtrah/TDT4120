class Vertex:
    def __init__(self, status, distance, parent, key):
        self.status = status
        self.distance = distance
        self.parent = parent
        self.key = key
        self.adjList = []

    def addAdjacentNodes(self, nodes):
        self.adjList = self.adjList + nodes


    def __str__(self):
        return "[" + str(self.key) + ", " + str(self.status) + ", " + str(self.distance) + ", " + (str(self.parent.key) if self.parent is not None else "") + "]"
