#!/usr/bin/env python

from algorithms import *

"""Solution to problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ddeg/
Problem: given an array of integers consituting a graph, return an array D[1..n] 
where D[i] is the sum of degrees of i's neighbors
"""
	
if __name__ == '__main__':
	f = open('data/rosalind_ddeg.txt','r').readlines()
	n = int (f[0].split()[0])

	dat = [list(map(int, f[i].split())) for i in range (1, len(f))]

	results  = doubleDegreeArray(n,dat)
	results = " ".join([str(results[i]) for i in range(1, len(results))])
	print results