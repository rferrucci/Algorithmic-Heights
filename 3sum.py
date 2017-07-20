#!/usr/bin/env python

from algorithms import *

"""Solution to 3SUM problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/3sum/
Problem: Given k arrays of size n, output a list of three indices i, j, k such 
that A[i] + A[j] + A[k] = 0 for each array A. Otherwise, output -1
"""

if __name__ == "__main__":	
	f = open('data/rosalind_3sum.txt','r').readlines()
	#o = open("ros_3sum.txt",'w')
	m, n = map(int, f[0].split())
	dat = [list(map(int, f[i].split())) for i in range (1, m+1)]
	for d in dat[0:]:
		result =ThreeSUM(n,d)
		if type(result) == int: print "%d" % result	
		else: print "%s" % " ".join([str(j) for j in result])
