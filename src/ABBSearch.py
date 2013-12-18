#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.key   = key
        self.children = 0

class ABBSearch(object):
    '''
    Arbol de busqueda binario
    '''
    def __init__(self):
        self.root = None

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