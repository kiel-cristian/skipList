#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Node(object):
    def __init__(self, parent, key):
        #Se mantiene referencia al padre para las rotaciones
        self.parent = parent
        self.left  = None
        self.right = None
        self.key   = key

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