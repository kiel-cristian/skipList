from random import randint

class ABB(object):
    def __init__(self):
        self.root = None
        self.nodes = 0

    def __len__(self):
        return self.nodes

    def addNode(self, key):
        comps = 0
        self.nodes += 1
        if self.root == None:
            self.root = Node(None, key)
            return (self.root, 1)
        node = self.root
        next = node
        while next != None:
            node = next
            if key < node.key:
                next = node.left
            else:
                next = node.right
            comps += 1
        newNode = Node(node, key)
        if key < node.key:
            node.left = newNode
        else:
            node.right = newNode
        return (node, comps)

    def add(self, key):
        return self.addNode(key)[1]

    def search(self, key):
        compares = 0
        node = self.root
        while node != None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
            compares += 1
        return (node, compares)

    def rotateRight(self, node):
        parent = node.parent
        node.parent = parent.parent
        parent.parent = node
        parent.left = node.right
        node.right = parent
        return node

    def rotateLeft(self, node):
        parent = node.parent
        node.parent = parent.parent
        parent.parent = node
        parent.right = node.left
        node.left = parent
        return node

class Node(object):
    def __init__(self, parent, key):
        "Se mantiene referencia al padre para las rotaciones"
        self.parent = parent
        self.left  = None
        self.right = None
        self.key   = key

class ABBRandom(ABB):

    def add(self, key):
        (node, comps) = self.addNode(key)
        if randint(1, self.nodes) == self.nodes:
            self.setAsRoot(node)
        return comps

    def setAsRoot(self, node):
        while node.parent != None:
            if node.parent.left == node:
                node = self.rotateRight(node)
            else:
                node = self.rotateLeft(node)
        self.root = node
        return node