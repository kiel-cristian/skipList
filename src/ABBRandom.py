from math import randint

class ABBTree(object):
    def add(self, key):
        pass
    def search(self, key):
        pass

class ABBNode(ABBTree):
    def __init__(self, left, rigth, key):
        self.left  = left
        self.rigth = rigth
        self.key   = key

    def add(self, key):
        if self.key < key:
            self.left  = self.left.add(key)
        else:
            self.rigth = self.rigth.add(key)
        return self

    def search(self, key):
        if self.key < key:
            return self.left.search(key)
        elif self.key > key:
            return self.rigth.search(key)
        else:
            return True
        return False

class ABBLeaf(ABBTree):
    def __init__(self, key = None):
        self.key   = key

    def add(self, key):
        new_self = self

        if self.key == None:
            new_self.key = key
        elif self.key < key:
            new_self = ABBNode(ABBLeaf(self.key), ABBLeaf(), key)
        else:
            new_self = ABBNode(ABBLeaf(), ABBLeaf(self.key), self.key)
        return new_self

    def search(self, key):
        if self.key == key:
            return True
        else:
            return False

class ABBRandom(ABBTree):
    def __init__(self):
        self.root = ABBLeaf()
        self.key_n    = 0

    def add(self, key):
        rand = randint(0, self.key_n)
        if rand == self.key_n:
            self.addOnRoot(key)
        else:
            self.root = self.root.add(key)
        self.key_n = self.key_n + 1

    def search(self, key):
        if self.root == None:
            return False
        else:
            return self.root.search(key)

    def addOnRoot(self, key):
        root_key = self.root.key
        self.root.key = key
        self.root = self.root.add(root_key)