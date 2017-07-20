#!/usr/bin/env python

def TwoSUM(dat):
	"""
	given an array of integers, if A[i] = -A[j], return indices i, j. else, return -1
	"""
	p = -1
	for i, v in enumerate(dat):
	 	if -v in dat:
			p = i + 1, dat.index(-v) + 1
			return p
	return p
	
def anagramSolution1(s1,s2):
	anagram = True
	s1 = list(s1)
	s2 = list(s2)
	s1.sort()
	s2.sort()

	if ''.join(s1) == ''.join(s2):
		return True
	else:
		return False