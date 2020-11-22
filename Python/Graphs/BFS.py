# Uses adjacency lists
# Will ALWAYS find the shortest path (or find out that there is no path at all)
# Will NOT necessarily visit all nodes
# if there are disjoint nodes or if there is no path to some nodes, it won't visit them
# This is unlike DFS, which will visit all nodes, but won't necessarily find the shortest path
import queue
import Algoritmer.Graphs.Vertex as Vertex

# G = A list of lists. G[0] contains for example [1,4,6] meaning that node 0 goes to nodes 1, 4 and 6.
def BFS(G, start):
    #setup
    for vertex in G:
        if vertex == None:
            continue
        vertex.status = "unseen"
        vertex.distance = -1
        vertex.parent = None
    start.status = "seen"
    start.distance = 0
    start.parent = None
    Q = queue.Queue(-1) # Queue that has an infinite size
    Q.put(start)
    #loop bröther
    while not Q.empty():
        u = Q.get()
        adjacentVertices = G[u.key].adjList
        for vertex in adjacentVertices:
            if vertex.status == "unseen":
                vertex.status = "seen"
                vertex.distance = u.distance + 1
                vertex.parent = u
                Q.put(vertex)
        u.status = "visited"


def print_path(G, start, end): # Prints path from start to end if it exists
    if start.key == end.key:
        print(start.key)
    elif end.parent is None:
        print("No path from " + str(start.key) + " to " + str(end.key))
    else:
        print_path(G,start,end.parent)
        print(end.key)

v1 = Vertex.Vertex("unseen",0, None, 1)
v2 = Vertex.Vertex("unseen",0, None, 2)
v3 = Vertex.Vertex("unseen",0, None, 3)
v4 = Vertex.Vertex("unseen",0, None, 4)
v5 = Vertex.Vertex("unseen",0, None, 5)
v6 = Vertex.Vertex("unseen",0, None, 6)

v1.addAdjacentNodes([v2,v3])
v3.addAdjacentNodes([v6])
v4.addAdjacentNodes([v6])
v5.addAdjacentNodes([v3,v4])

graph = [None,v1,v2,v3,v4,v5,v6]

BFS(graph, v1)

for vertex in graph:
    if vertex is None:
        continue
    print(vertex)
print("\n\n")
print_path(graph,v1,v6)









