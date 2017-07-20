#!/usr/bin/env python

from algorithms import *

"""Solution to Degree Array problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ddeg/
Problem: given an array of integers consituting a graph, return an array D[1..n] 
where D[i] is the sum of degrees of i's neighbors
"""
		
if __name__ == "__main__":
	f = open("data/rosalind_deg.txt",'r').readlines()	
	n,m = map(int,f[0].split())
	edges = [map(int,f[i].split()) for i in xrange(1,m+1)]
	deg = degreeArray(n, edges)
	print (deg)
