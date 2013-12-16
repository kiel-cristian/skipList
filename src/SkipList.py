#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, seed

class SkipNode(object):
    '''
    Nodo de SkipList
    '''
    def __init__(self, height = 0, key = None):
        self.key = key
        self.next = [None]*height

class SkipList(object):
    '''
    Skip List
    '''
    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.max_height = 0

    def __len__(self):
        return self.len

    def closest_nodes(self, key):
        '''
        Entrega los nodos más cercanos al valor de 'key' por la izquierda, en todos los niveles.
        ie. update[0] contendrá al nodo inmediatamente anterior al que contiene a 'key' o la sobrepasa
        (en caso de que no esté presente), en la lista más 'baja'.
        '''
        update = [None]*self.max_height
        comparisons = 0
        node_x = self.head
        for i in reversed(range(self.max_height)):
            while node_x.next[i] != None and node_x.next[i].key < key:
                node_x = node_x.next[i]
                comparisons += 1
            update[i] = node_x
        return (update, comparisons)

    def add(self, key):
        '''
        Inserta un elemento y retorna el numero de comparaciones que se hicieron
        '''
        node = SkipNode(self.random_height(), key)

        self.max_height = max(self.max_height, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        (update, comparisons) = self.closest_nodes(key)
        if self.search(key, update)[0] == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

        return comparisons

    def search(self, key, update = None):
        '''
        Busca un elemento y lo retorna si lo encuentra, o None si no. Tambien entrega las comparaciones realizadas
        '''
        comparisons = 0
        if update == None:
            (update, comparisons) = self.closest_nodes(key)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.key == key:
                return (candidate, comparisons)
        return (None, comparisons)

    def random_height(self):
        '''
        Altura aleatoria para nuevo nodo
        '''
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height