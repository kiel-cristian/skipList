from random import randint

class ABB(object):
    def __init__(self):
        self.root = None
        self.nodes = 0

    def addNode(self, key):
        self.nodes += 1
        if self.root == None:
            self.root = Node(None, key)
            return self.root
        node = self.root
        next = node
        while next != None:
            node = next
            if key < node.key:
                next = node.left
            else:
                next = node.right
        newNode = Node(node, key)
        if key < node.key:
            node.left = newNode
        else:
            node.right = newNode
        return newNode

    def add(self, key):
        self.addNode(key)
        return self

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
        self.parent = parent    "Se mantiene referencia al padre para las rotaciones"
        self.left  = None
        self.right = None
        self.key   = key

class ABBRandom(ABB):

    def add(self, key):
        node = self.addNode(key)
        if randint(1, self.nodes) == self.nodes:
            self.setAsRoot(node)
        return self

    def setAsRoot(self, node):
        while node.parent != None:
            if node.parent.left == node:
                node = self.rotateRight(node)
            else:
                node = self.rotateLeft(node)
        self.root = node
        return node