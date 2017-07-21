#!/usr/bin/env python

from rosalind import *

"""Solution to Longest Increasing Subsequence problem in the Algorithmic Heights  
section of Rosalind
location: http://rosalind.info/problems/lgis/
Problem: Given k arrays of size n, output a list of paired indices i, j such that 
A[i] = -A[j] for each array A. Otherwise, output -1
"""

def longestIncreasingSubsequence(n, seq):
	P = [None for i in range(n)]
	M = [None for i in range(n + 1)]
	L = 0

	for i in range(n):
		lo = 1
		hi = L
		
		while (lo <= hi):
			mid = (lo+hi)/2
			if seq[M[mid]] < seq[i]:
				lo = mid + 1
			else:
				hi = mid - 1
			
		newL = lo
		P[i] = M[newL - 1]
		M[newL] = i

		if newL > L:
			L = newL
	
	S = []
	k = M[L]
	for i in range(L-1, -1, -1):
		S.append(seq[k])

		k = P[k]

	return(S[::-1])
		
if __name__ == "__main__":
	f = open('data/rosalind_lgis.txt','r').readlines()

	n = int(f[0].strip())
	seq = map(int, f[1].split())
	inc = longestIncreasingSubsequence(len(seq), seq)
	seq.reverse()
	dec = longestIncreasingSubsequence(len(seq), seq)
	dec.reverse()
	print ' '.join(map(str, inc))
	print ' '.join(map(str, dec))
