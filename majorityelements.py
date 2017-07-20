#!/usr/bin/env python

from algorithms import *

"""Solution to problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ddeg/
Problem: Given an array of integers, return element that is found more than n/2
times. Else, return -1
"""
		
if __name__ == "__main__":
	f = open('data/rosalind_maj.txt','r').readlines()
	m, n = map(int, f[0].split())
	A = [(map(int, f[i].split())) for i in range(1, len(f))]
	A = majorityElement(n, A)
	print " ".join([str(a) for a in A])