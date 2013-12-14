
class ABBTree(object):
    def __init__(self):
        self.key = None
        self.compares = 0
    def add(self, key):
        pass
    def search(self, compares, key):
        pass
    def setKey(self, key):
        pass

class ABBNode(ABBTree):
    def __init__(self, left, right, key):
        super(ABBNode, self).__init__()
        self.left  = left
        self.right = right
        self.key   = key

    def add(self, key):
        if self.key > key:
            self.left  = self.left.add(key)
        else:
            self.right = self.right.add(key)
        return self

    def search(self, compares, key):
        new_compares = compares

        if self.key > key:
            new_compares = new_compares + 1
            return self.left.search(new_compares, key)
        elif self.key < key:
            new_compares = new_compares + 1
            return self.right.search(new_compares, key)

        return ABBSearch(new_compares, True)

    def setKey(self, key):
        self.key = key
        return self

class ABBLeaf(ABBTree):
    def __init__(self, key):
        super(ABBLeaf, self).__init__()
        self.key   = key

    def add(self, key):
        new_self = self

        if self.key < key:
            new_self = ABBNode(ABBEmptyLeaf(), ABBLeaf(key), self.key)
        else:
            new_self = ABBNode(ABBLeaf(key), ABBEmptyLeaf(), self.key)

        return new_self

    def search(self, compares, key):
        new_compares = compares + 1
        if self.key == key:
            return ABBSearch(new_compares, True)
        else:
            return ABBSearch(new_compares, False)

    def setKey(self, key):
        self.key = key
        return self

class ABBEmptyLeaf(ABBTree):
    def add(self, key):
        return ABBLeaf(key)

    def setKey(self, key):
        return ABBLeaf(key)

    def search(self, compares, key):
        return ABBSearch(0, False)

class ABBSearch(object):
    def __init__(self, compares, found):
        self.compares = compares
        self.found  = found