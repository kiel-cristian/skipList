
from ABBTree import *

class ABB(object):
    def __init__(self):
        self.root  = ABBEmptyLeaf()
        self.key_n = 0

    def add(self, key):
        self.root = self.root.add(key)
        self.key_n = self.key_n + 1

    def search(self, key):
        return self.root.search(0, key)