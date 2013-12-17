from random import randint
from SkipList import *
from ABB import *

def random_sequence(length, max_n):
    '''
    Retorna una secuencia ordenada de enteros entre 0 y "max_n", de largo "length"
    '''
    seq = []
    num = 0
    while len(seq) < length:
        if num > max_n:
            seq = []
            num = 0

        if randint(0, max_n) <= length:
            seq.append(num)

        num += 1
    return seq

def k_swaps(seq, k):
    '''
    Cambios de elementos en el arreglo
    '''
    new_seq = list(seq)
    for j in range(0, k):
        sequence_1 = randint(0, len(seq)-1)
        sequence_2 = randint(0, len(seq)-1)
        new_seq[sequence_1] = seq[sequence_2]
        new_seq[sequence_2] = seq[sequence_1]
    return new_seq

def main():
    '''
    Pricipal
    '''
    abb_tree  = ABB()
    abbr_tree = ABBRandom()
    skip_list = SkipList()
    sequence = random_sequence(10000, 100000)

    for i in sequence:
        abb_tree.insert(i)
        abbr_tree.insert(i)
        skip_list.insert(i)
    return (abb_tree, abbr_tree, skip_list)

if __name__ == "__main__":
    main()