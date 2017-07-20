#!/usr/bin/env python

from algorithms import *

"""Solution to problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ins/
Problem: returns number of swaps needed to sort array using insertion sort
"""

if __name__ == "__main__":
	f = open('data/rosalind_ins.txt','r').readlines()
	dat = [int(i) for i in f[1].split()]
	n = insertionSort(dat)
	print n