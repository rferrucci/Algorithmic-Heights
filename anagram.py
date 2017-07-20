#!/usr/bin/env python

from algorithms import *
"""Solution to problem in the Algorithmic Heights section of Rosalind
location: http://rosalind.info/problems/ddeg/
Problem: given an array of integers consituting a graph, return an array D[1..n] 
where D[i] is the sum of degrees of i's neighbors
"""


s1 = 'ceart'
s2 = 'earth'

if __name__ == "__main__":
	if len(s1) == len(s2):
		print (anagramSolution1(s1,s2))
	else:
		print "different lengths"
