
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
    def __init__(self, left, rigth, key):
        super(ABBNode, self).__init__()
        self.left  = left
        self.rigth = rigth
        self.key   = key

    def add(self, key):
        if self.key < key:
            self.left  = self.left.add(key)
        else:
            self.rigth = self.rigth.add(key)
        return self

    def search(self, compares, key):
        new_compares = compares

        if self.key < key:
            new_compares = new_compares + 1
            return self.left.search(new_compares, key)
        elif self.key > key:
            new_compares = new_compares + 1
            return self.rigth.search(new_compares, key)

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
            new_self = ABBNode(ABBLeaf(self.key), ABBLeaf(), key)
        else:
            new_self = ABBNode(ABBLeaf(), ABBLeaf(self.key), self.key)

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
    def __init__(self, compares, founded):
        self.compares = compares
        self.founded  = founded