#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from SkipList import *
from ABB import *
from ABBRandom import *

class RandomSequence(object):
    '''
    Estructura de datos que mantiene una secuencia ordenada de enteros entre 0 y "max_n", de largo "length"
    '''
    def __init__(self, length, max_n):
        (self.elements, self.free_elements) = self.random_sequence(length, max_n)
        self.f_length = len(self.free_elements)
        self.max_n  = max_n
        self.length = length

    def random_sequence(self, length, max):
        elements = []
        free_elements = []
        num = 0
        while len(elements) < length:
            if num > max:
                elements = []
                free_elements = []
                num = 0
            if randint(0, max) <= length:
                elements.append(num)
            else:
                free_elements.append(num)
            num +=1
        return (elements, free_elements)

    def get_element(self, elem):
        '''
        Retorna el elemento en la posicion elem
        '''
        return self.elements[elem]

    def get_random_element(self):
        '''
        Obtiene un elemento aleatorio que se encuentra en la secuencia
        '''
        return self.elements[randint(0, self.length - 1)]

    def get_random_free_element(self):
        '''
        Obtiene un elemento aleatorio que no se encuentra en la secuencia
        '''
        return self.free_elements[randint(0, self.f_length - 1)]

    def k_swaps(self, k):
        '''
        Cambios de elementos en el arreglo
        '''
        new_seq = list(self.elements)
        for i in range(0, k):
            first_element = randint(0, self.length - 1)
            second_element = randint(0, self.length - 1)
            new_seq[first_element] = self.elements[second_element]
            new_seq[second_element] = self.elements[first_element]
        return new_seq

def getTestData():
    a = ABB()
    r = ABBRandom()
    seq = RandomSequence(10**4, 10**5)
    k = int(0.005*seq.length)
    abb_seq = seq.k_swaps(k)
    for i in range(0, seq.length):
        a.insert(abb_seq[i])
        r.insert(seq.get_element(i))
    return (a, r)

def main(elements, adjust):
    '''
    Principal
    '''
    insertions         = elements
    searches           = int(0.5*elements)
    not_found_searches = int(0.25*searches)
    swaps_amount       = int(0.005*elements)
    init               = False
    sequence           = RandomSequence(elements, 10**5)
    iteration          = 0
    mean_height        = 0

    while (not init) or abb_comps - abbr_comps > abbr_comps*adjust:
        if not init:
            init = True

        # Número de iteracion para acercar comportamiento de árboles
        iteration += 1
        print('iteration: ' + str(iteration))

        # Contadores
        abb_comps    = 0
        abbr_comps   = 0
        skip_comps   = 0

        abb_search_comps    = 0
        abbr_search_comps   = 0
        skip_search_comps   = 0

        # Se definen las estructuras
        abb_tree  = ABB()
        abbr_tree = ABBRandom()
        skip_list = SkipList()

        # Lista para ABB
        abb_elements = sequence.k_swaps(swaps_amount)

        # Inserciones
        for i in range(insertions):
            abb_comps  += abb_tree.insert(abb_elements[i])
            abbr_comps += abbr_tree.insert(sequence.get_element(i))
            skip_comps += skip_list.insert(sequence.get_element(i))

        # Busquedas
        for i in range(searches):
            if i < not_found_searches:
                elem = sequence.get_random_free_element()
            else:
                elem = sequence.get_random_element()
            abb_search_comps  += abb_tree.search(elem)[1]
            abbr_search_comps += abbr_tree.search(elem)[1]
            skip_search_comps += skip_list.search(elem)[1]

        # Altura de skip list
        mean_height += skip_list.max_height

        # Siguiente iteración
        sequence.elements = abb_elements

    # Resultados: Inserciones
    abb_comps  = abb_comps/insertions
    abbr_comps = abbr_comps/insertions
    skip_comps = skip_comps/insertions

    # Resultados: Busquedas
    abb_search_comps  = abb_search_comps/searches
    abbr_search_comps = abbr_search_comps/searches
    skip_search_comps = skip_search_comps/searches

    # Resultados: Altura de Skip List
    mean_height = mean_height/iteration

    print('insertions: ' + str(abb_comps) + ',' + str(abbr_comps) + ',' + str(skip_comps))
    print('searches: ' + str(abb_search_comps) + ',' + str(abbr_search_comps) + ',' + str(skip_search_comps))
    print('skiplist height: ' + str(mean_height))
    print('iterations: ' + str(iteration))
    print('swaps: ' + str(swaps_amount) + '\n')
    print('total swaps: ' + str(swaps_amount*iteration))


if __name__ == "__main__":
    for elements in [10**4 , 2*10**4 , 5*10**4]:
        print('n :' + str(elements))
        main(elements, 0.10)
