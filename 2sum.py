#!/usr/bin/env python

from algorithms import *

"""Solution to 2SUM problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/2sum/
Problem: Given k arrays of size n, output a list of paired indices i, j such that 
A[i] = -A[j] for each array A. Otherwise, output -1
"""
if __name__ == "__main__":
	f = open('data/rosalind_2sum.txt','r').readlines()
	o = open("ros_2sum.txt",'w')
	m, n = map(int, f[0].split())
	dat = [list(map(int, f[i].split())) for i in range (1, m+1)]
	for d in dat:
		result =TwoSUM(d)
		if type(result) == int: print "%d" % result	
		else: print "%s" % " ".join([str(j) for j in result])
