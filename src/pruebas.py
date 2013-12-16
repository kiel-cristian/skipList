from random import randint
from SkipList import *
from ABBIter import *

def randomSequence(length, max):
	"Retorna una secuencia ordenada de enteros entre 0 y 'max', de largo 'length'"
	seq = []
	num = 0
	while len(seq) < length:
		if num > max:
			seq = []
			num = 0

		if randint(0, max) <= length:
			seq.append(num)

		num +=1
	return seq

def kSwaps(seq, k):
	newSeq = list(seq)
	for i in range(0, k):
		s1 = randint(0, len(seq)-1)
		s2 = randint(0, len(seq)-1)
		newSeq[s1] = seq[s2]
		newSeq[s2] = seq[s1]
	return newSeq

def main():
	a = ABB()
	r = ABBRandom()
	s = SkipList()
	l = randomSequence(10000, 100000)
	for i in l:
		a.add(i)
		r.add(i)
		s.add(i)
	return (a, r, s)

if __name__ == "__main__":
	main()