
class ABBTree(object):
    '''
    Arbol binario polimórfico
    '''
    def __init__(self):
        self.key = None
        self.compares = 0
    def insert(self, key):
        '''
        Inserta una clave en el tipo de nodo en cuestion (nodo, hoja u hoja vacía)
        '''
        pass
    def insert_on_root(self, parent, key):
        '''
        Inserta una clave en la raíz del árbol, y para eso, se efectúa una inserción normal y luego
        se efectúan rotaciones hasta dejar la clave en la raíz.
        '''
        pass
    def search(self, compares, key):
        '''
        Busca una clave en el árbol, generando un ABBSearch como resultado
        '''
        pass
    def set_key(self, key):
        '''
        Actualiza el valor de la clave actual
        '''
        pass

class ABBNode(ABBTree):
    '''
    Nodo
    '''
    def __init__(self, left, rigth, key):
        super(ABBNode, self).__init__()
        self.left  = left
        self.rigth = rigth
        self.key   = key

    def insert_on_root(self, parent, key, parent_type = 'Any'):
        if self.key < key:
            self.left = self.left.insert_on_root(self, key, 'R')
        else:
            self.rigth = self.rigth.insert_on_root(self, key, 'L')

        if parent_type == 'R':
            if key 
        elif parent_type == 'L':
        else:
            return self

    def insert_on_root_by_left

    def insert(self, key):
        if self.key < key:
            self.left  = self.left.insert(key)
        else:
            self.rigth = self.rigth.insert(key)
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

    def set_key(self, key):
        self.key = key
        return self

class ABBLeaf(ABBTree):
    '''
    Hoja
    '''
    def __init__(self, key):
        super(ABBLeaf, self).__init__()
        self.key   = key

    def insert(self, key):
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

    def set_key(self, key):
        self.key = key
        return self

class ABBEmptyLeaf(ABBTree):
    '''
    Hoja vacía
    '''
    def insert(self, key):
        return ABBLeaf(key)

    def set_key(self, key):
        return ABBLeaf(key)

    def search(self, compares, key):
        return ABBSearch(0, False)

class ABBSearch(object):
    '''
    Resultado de búsqueda, contiene número de comparaciones de claves y resultado (True o False)
    '''
    def __init__(self, compares, founded):
        self.compares = compares
        self.founded  = founded