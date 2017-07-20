#!/usr/bin/env python

from algorithms import *

"""Solution to Binary Search problem in the Algorithmic Heights section of 
Rosalind 
location: http://rosalind.info/problems/bins/
Problem: Given two arrays, A and B, output indice in sorted array A for integer
in array B. Else, output - 1
"""

"""finds location in sorted list of given item
"""

if __name__ == "__main__":
	l = ""
	f = open('data/rosalind_bins.txt','r').readlines();
	n,m = int(f[0]),int(f[1	])
	A = map(int, f[2].split())
	B = map(int, f[3].split())

	for b in range(len(B)):
		l += '%d ' % (binSearch(A, B[b]))

	print l
