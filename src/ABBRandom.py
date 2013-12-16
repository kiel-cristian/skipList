
from random import randint
from ABBTree import *

class ABBRandom(object):
    '''
    Cabezera de árbol binario aleatorizado
    '''
    def __init__(self):
        self.root  = ABBEmptyLeaf()
        self.key_n = 0

    def insert(self, key):
        '''
        Inserción aleatorizada, inserta con probabilidad 1/n en la raíz, si no,
        se efectúa una inserción normal
        '''
        rand = randint(0, self.key_n)

        if rand == self.key_n:
            # Insercion en la raíz
            self.root = self.root.insert_on_root(self.root, key)
        else:
            # Inserción normal
            self.root = self.root.insert(key)

        self.key_n = self.key_n + 1

    def search(self, key):
        '''
        Búsqueda en el árbol común
        '''
        return self.root.search(0, key)