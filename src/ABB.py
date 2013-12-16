#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ABBTree import *

class ABB(object):
    '''
    Arbol de búsqueda binario (con cabecera y meta datos)
    '''
    def __init__(self):
        self.root = None
        self.nodes = 0

    def add_node(self, key):
        '''
        Agrega un nodo en el árbol raíz actual
        '''
        comps = 0
        self.nodes += 1
        if self.root == None:
            self.root = Node(None, key)
            return (self.root, 1)
        node = self.root
        next = node
        while next != None:
            node = next
            if key < node.key:
                next = node.left
            else:
                next = node.right
            comps += 1
        new_node = Node(node, key)
        if key < node.key:
            node.left = new_node
        else:
            node.right = new_node
        return (node, comps)

    def insert(self, key):
        '''
        Inserta un nodo en el árbol
        '''
        return self.add_node(key)[1]

    def search(self, key):
        '''
        Busca la clave en el arbol
        '''
        compares = 0
        node = self.root
        while node != None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
            compares += 1
        return (node, compares)