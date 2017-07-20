#!/usr/bin/env python

from algorithms import *

"""Solution to Merge Sort problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ddeg/
Problem: given two sorted array of integers, return a single sorted array
"""
		
if __name__ == "__main__":
	f = open('data/rosalind_mer.txt','r').readlines()
	A = list(map(int, f[1].split()))
	B = list(map(int, f[3].split()))
	C = mergeSort(A, B)

	print " ".join([str(c) for c in C])
