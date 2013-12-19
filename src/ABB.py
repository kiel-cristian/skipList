#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Node(object):
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.key   = key
        self.children = 0

class ABB(object):
    '''
    Arbol de búsqueda binario (con cabecera y meta datos)
    '''
    def __init__(self):
        self.root = None

    def add_node(self, key):
        '''
        Agrega un nodo en el árbol raíz actual
        '''
        comps = 0
        if self.root == None:
            self.root = Node(key)
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
    Cabecera de árbol binario aleatorizado
    '''
    def __init__(self):
        super(ABBRandom, self).__init__()

    def insert(self, key):
        (self.root, comps) = self.insert_rec(self.root, key)
        return comps

    def insert_rec(self, node, key):
        '''
        Inserción aleatorizada, inserta con probabilidad 1/(n+1) en la raíz del
        sub-árbol cuya raíz actual es "node".
        '''
        if node == None:
            return (Node(key), 0)
        if randint(0, node.children + 1) == node.children:
            return self.insert_at_root(node, key)
        if key < node.key:
            (node.left, comps) = self.insert_rec(node.left, key)
        else:
            (node.right, comps) = self.insert_rec(node.right, key)
        node.children += 1
        return (node, comps + 1)

    def insert_at_root(self, node, key):
        '''
        Inserta un nodo de llave "key" en la raíz de este sub-árbol,
        cuya raíz actual es "node".
        '''
        if node == None:
            return (Node(key), 0)
        if key < node.key:
            (node.left, comps) = self.insert_at_root(node.left, key)
            node = self.rotate_right(node)
        else:
            (node.right, comps) = self.insert_at_root(node.right, key)
            node = self.rotate_left(node)
        return (node, comps + 1)

    def count_children(self, node):
        '''
        Cuenta los hijos de un nodo dado
        '''
        if node.left == None:
            left = 0
        else:
            left = node.left.children + 1
        if node.right == None:
            right = 0
        else:
            right = node.right.children + 1
        return left + right

    def rotate_left(self, node):
        '''
        Rotacion de nodo derecho con respecto a su padre
        '''
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        node.children = self.count_children(node)
        new_node.children = self.count_children(new_node)
        return new_node

    def rotate_right(self, node):
        '''
        Rotacion de nodo izquierdo con respecto a su padre
        '''
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        node.children = self.count_children(node)
        new_node.children = self.count_children(new_node)
        return new_node

if __name__ == '__main__':
    abb = ABB()
    abb_r = ABBRandom()
    for i in range(1,1000):
        abb.insert(i)
        abb_r.insert(i)