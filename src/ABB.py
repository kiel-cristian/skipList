
from ABBTree import *

class ABB(object):
    '''
    Cabezera de árbol binario
    '''
    def __init__(self):
        self.root  = ABBEmptyLeaf()
        self.key_n = 0

    def insert(self, key):
        '''
        Inserción de una clave, aumenta en 1 el número de llaves
        '''
        self.root = self.root.insert(key)
        self.key_n = self.key_n + 1

    def search(self, key):
        '''
        Búsqueda en el árbol común
        '''
        return self.root.search(0, key)