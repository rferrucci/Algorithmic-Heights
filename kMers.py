#!/usr/bin/env python

from algorithms import *
import itertools
"""Solution to Enumerating k-mers Lexicographically problem in the  
Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/lexf/
Problem: Given k arrays of size n, output a list of paired indices i, j such that 
A[i] = -A[j] for each array A. Otherwise, output -1
"""
if __name__ == "__main__":
	f = open('data/rosalind_lexf.txt','r').readlines()
	symb = f[0].split()
	n = int(f[1].strip())
	
	perm = kMer(symb, n)
	
	for i in perm:
		print (i)