#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from ABB import *

class ABBRandom(ABB):
    '''
    Cabezera de árbol binario aleatorizado
    '''
    def __init__(self):
        super(ABBRandom, self).__init__()

    def insert(self, key):
        '''
        Inserción aleatorizada, inserta con probabilidad 1/n en la raíz, si no,
        se efectúa una inserción normal
        '''
        (node, comps) = self.add_node(key)
        if randint(1, self.nodes) == self.nodes:
            self.set_as_root(node)
        return comps

    def rotate_right(self, node):
        '''
        Rotacion de nodo derecho con respecto a su padre
        '''
        parent = node.parent
        node.parent = parent.parent
        parent.parent = node
        parent.left = node.right
        node.right = parent
        return node

    def rotate_left(self, node):
        '''
        Rotacion de nodo izquierdo con respecto a su padre
        '''
        parent = node.parent
        node.parent = parent.parent
        parent.parent = node
        parent.right = node.left
        node.left = parent
        return node

    def set_as_root(self, node):
        '''
        Cambia el valor de la raíz por la ultima clave insertada
        '''
        while node.parent != None:
            if node.parent.left == node:
                node = self.rotate_right(node)
            else:
                node = self.rotate_left(node)
        self.root = node
        return node

