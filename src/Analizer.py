#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

def compute_mean(data_list):
    '''
    Calcula el promedio dada una lista de datos
    '''
    return reduce(lambda x, y: x + y, data_list) / len(data_list)

def compute_errors(data_list, data_means, max_n):
    '''
    Calcula el error de una lista de datos de tamaño "max_n"
    '''
    data_list_len = len(data_list)
    error_data_lists = [0 for e in range(data_list_len)]

    for i in range(max_n):
        for k in range(data_list_len):
            error_data_lists[k] += (data_means[k] - data_list[k][i])**2

    for i in range(data_list_len):
        error_data_lists[i] = sqrt(error_data_lists[i])
    return error_data_lists

class ADTAnalyzer(object):
    '''
    Acumula los datos de una estructura de datos, luego de encontrar el ajuste entre ABB y ABBRandom
    '''
    def __init__(self, max_n):
        self.insertions = []
        self.searches   = []

        self.mean_insertion = 0
        self.error_insertion = 0

        self.mean_search = 0
        self.error_search = 0

        self.max_n = max_n

    def __str__(self):
        return '\n\t i: ' + str(self.mean_insertion) + ' +- ' + str(self.error_insertion) + '\n\t s: ' + str(self.mean_search) + ' +- ' + str(self.error_search)

    def add_result(self, insertions, searches):
        '''
        Agrega una tupla de resultados (inserciones, busquedas, swaps)
        '''
        # Costo por operacion de inserciones
        self.insertions += [insertions]

        # Costo por operacion de busquedas
        self.searches   += [searches]

    def compute_errors(self):
        '''
        Calcula la desviacion estandar de las inserciones y busquedas
        '''
        self.mean_insertion = compute_mean(self.insertions)
        self.mean_search    = compute_mean(self.searches)
        (self.error_insertion, self.error_search) = compute_errors([self.insertions, self.searches], [self.mean_insertion, self.mean_search], self.max_n)

class ExperimentAnalyzer(object):
    '''
    Analizador global del experimento
    '''
    def __init__(self, max_n):
        self.swaps = []
        self.mean_swaps = 0
        self.error_swaps = 0

        self.skip_heights = []
        self.mean_skip_height = 0
        self.error_skip_height = 0

        self.max_n = max_n

        self.abb_analizer       = ADTAnalyzer(max_n)
        self.abbr_analizer      = ADTAnalyzer(max_n)
        self.skip_list_analizer = ADTAnalyzer(max_n)

    def add_abb_result(self, ins, search, swaps):
        ''''
        Se agregan datos al analizer de resultados ABB
        '''
        self.abb_analizer.add_result(ins, search)

        # Manejo de swaps aplicados al input
        self.swaps += [swaps]

    def add_abbr_result(self, ins, search):
        '''
        Se agregan datos al analizer de resultados ABBRandom
        '''
        self.abbr_analizer.add_result(ins, search)

    def add_skip_list_result(self, ins, search, height):
        '''
        Se agregan datos al analizer de resultados Skip List
        '''
        self.skip_list_analizer.add_result(ins, search)

        # Manejo de altura de skip list
        self.skip_heights += [height]

    def compute_errors(self):
        self.abb_analizer.compute_errors()
        self.abbr_analizer.compute_errors()
        self.skip_list_analizer.compute_errors()

        self.mean_swaps = compute_mean(self.swaps)
        self.mean_skip_height = compute_mean(self.skip_heights)
        (self.error_swaps, self.error_skip_height) = compute_errors([self.swaps, self.skip_heights], [self.mean_swaps, self.mean_skip_height], self.max_n)

    def show_results(self):
        print('ABB:' + str(self.abb_analizer))
        print('ABBR:' + str(self.abbr_analizer))
        print('SkipList:' + str(self.skip_list_analizer))
        print('Swaps: ' + str(self.mean_swaps) + ' +- ' + str(self.error_swaps))
        print('SList heigth: ' + str(self.mean_skip_height) + ' +- ' + str(self.error_skip_height))

if __name__ == '__main__':
    means = [0, 0, 0]
    datas = [[1.0,1.2,1.3,1.5], [5.1, 5.3, 5.5, 5.5], [7.4, 7.5, 7.4, 7.6]]

    total_datas = len(datas)
    data_len = len(datas[0])

    for k in range(total_datas):
        means[k] = compute_mean(datas[k])
    errors = compute_errors(datas, means, data_len)

    for i in range(total_datas):
        print(str(means[i]) + ' +-' + str(errors[i]))

    exps = 10
    exp = ExperimentAnalyzer(exps)

    from random import randint

    # Simulacion de datos
    #ABB
    abb_i_data = [randint(40, 43) for i in range(exps)]
    abb_s_data = [randint(41, 45) for i in range(exps)]
    swap_data  = [randint(10, 15) for i in range(exps)]

    #ABBR
    abbr_i_data = [randint(30,33) for i in range(exps)]
    abbr_s_data = [randint(31,35) for i in range(exps)]

    #SkipList
    skip_i_data = [randint(25,30) for i in range(exps)]
    skip_s_data = [randint(23,28) for i in range(exps)]
    height_data = [randint(12,14) for i in range(exps)]

    print('ABB data:')
    print('i: ' + str(abb_i_data)),
    print('s: ' + str(abb_s_data)),
    print('sw: ' + str(swap_data))

    print('ABBR data:')
    print('i: ' + str(abbr_i_data)),
    print('s: ' + str(abbr_s_data))

    print('SkipList data:')
    print('i: ' + str(skip_i_data)),
    print('s: ' + str(skip_s_data)),
    print('h: ' + str(height_data))

    for i in range(10):
        exp.add_abb_result(abb_i_data[i], abb_s_data[i], swap_data[i])
        exp.add_abbr_result(abbr_i_data[i], abbr_s_data[i])
        exp.add_skip_list_result(skip_i_data[i], skip_s_data[i], height_data[i])
    exp.compute_errors()
    exp.show_results()
