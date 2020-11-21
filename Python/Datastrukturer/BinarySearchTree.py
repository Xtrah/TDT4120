# Binary search tree property: Left node is smaller than parent, right node is larger than parent
import random
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

class BinaryTree:

    def __init__(self, root):
        self.root = root

    def inorder_tree_walk(self, root): # Writes all numbers in increasing order
        if root is not None:
            self.inorder_tree_walk(root.left)
            print("Key: " + str(root.key) + ", left: " + str(root.left) + ", right: " + str(root.right) + ", parent: " + str(root.parent))
            self.inorder_tree_walk(root.right)

    def tree_minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    def tree_maximum(self, root):
        while root.right is not None:
            root = root.right
        return root

    def tree_search(self, root, key):
        while root is not None and key is not root.key:
            if key < root.key:
                root = root.left
            else:
                root = root.right
        return root

    def tree_successor(self, node): # Returns the node with the bigger key than the argument node
        if node.right is not None:
            return self.tree_minimum(node.right)
        p = node.parent
        while p is not None and node is p.right:
            # "Go up one level"
            node = p
            p = p.parent
        return p


    def insert(self, T, node):
        y = None
        root = T.root
        while root is not None:
            y = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right
        node.parent = y
        if y is None: # The new node is the root
            T.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def transplant(self, T, u, v): # Replaces subtree rooted at u with subtree rooted at v
        if u.parent == None:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, T, node):
        if node.left is None:
            self.transplant(T,node,node.right) # Swap out subtree rooted at node with subtree rooted at node.right
        elif node.right is None:
            self.transplant(T, node, node.left)  # Swap out subtree rooted at node with subtree rooted at node.right
        else:
            y = self.tree_minimum(node.right)
            if y.parent != node:
                self.transplant(T,y,y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(T,node,y)
            y.left = node.left
            y.left.parent = y








rootNode = Node(5)
binTree = BinaryTree(rootNode)
nodeList = [rootNode]
for i in range(5):
    n = Node(random.randint(-10,10))
    nodeList.append(n)
    binTree.insert(binTree, n)


print(nodeList)
print("Before:")
binTree.inorder_tree_walk(binTree.root)
print("\n")
print("After:")
print(type(nodeList[0]))
binTree.delete(binTree,nodeList[0])
binTree.inorder_tree_walk(binTree.root)

