
from random import randint
from ABBTree import *

class ABBRandom(object):
    def __init__(self):
        self.root  = ABBEmptyLeaf()
        self.key_n = 0

    def add(self, key):
        rand = randint(0, self.key_n)

        if rand == self.key_n:
            self.addOnRoot(key)
        else:
            self.root = self.root.add(key)

        self.key_n = self.key_n + 1

    def search(self, key):
        return self.root.search(0, key)

    def addOnRoot(self, key):
        root_key = self.root.key
        self.root = self.root.setKey(key)
        if root_key != None:
            self.root = self.root.add(root_key)