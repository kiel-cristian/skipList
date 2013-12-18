#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ABBSearch import *

class ABB(ABBSearch):
    '''
    Arbol de búsqueda binario (con cabecera y meta datos)
    '''
    def __init__(self):
        super(ABB, self).__init__()

    def add_node(self, key):
        '''
        Agrega un nodo en el árbol raíz actual
        '''
        comps = 0
        if self.root == None:
            self.root = Node(key)
            return 1

        node = self.root
        next = node

        while next != None:
            node = next
            if key < node.key:
                next = node.left
            else:
                next = node.right
            comps += 1
        new_node = Node(key)
        if key < node.key:
            node.left = new_node
        else:
            node.right = new_node
        return comps

    def insert(self, key):
        '''
        Inserta un nodo en el árbol
        '''
        return self.add_node(key)

if __name__ == '__main__':
    abb_tree = ABB()
    for i in range(1, 1000):
        abb_tree.insert(i)