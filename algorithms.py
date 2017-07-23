#!/usr/bin/env python

from collections import defaultdict
import itertools
"""Methods for Algorithmic Heights solutions
"""

def insertionSort(A):
	"""sorts an array A using the insertion sort algorithim, returns number of 
	swaps requried as well as sorted list
	"""
	n = 0
	for i in range(1, len(A)):
		k = i
		while k > 0 and A[k] < A[k-1]:
			tmp = A[k-1]
			A[k-1] = A[k]
			A[k] = tmp
			k -= 1
			n +=1

	return n, A

def kMer(symb, n):
	""" takes array of symbols and returns all permutations of length n
	"""
	
	prod = itertools.product(symb, repeat=n)
	perm=[]
	for p in prod:
		perm.append(''.join(p))	
	perm.sort()
	return perm

def mergeSort(A, B):
	"""	merges two sorted arrays into a second sorted array
	"""
	C = []
	
	"""compares first element of A with first element of B. Whichever is smallest
	gets added to new array C and removed from it's original array until one of 
	the original arrays are empty"""
	while len(A) > 0 and len(B) > 0:
		if A[0] < B[0]:
			C.append(A.pop(0))
		else:
			C.append(B.pop(0))
	
	#then we add remaining elements from each array to the new array		
	C.extend(A)
	C.extend(B)

	return C

def majorityElement(n, A):
	"""from a list of arrays, determines prescence of majority elements
	"""
	Maj = []
	for a in A:
		"""set maj to -1. If a majority element exists, maj is set to it."""
		maj = -1
		for i in set(a):
			if a.count(i) > n/2.0:
				maj = i
		Maj.append(maj)
	return Maj

def degreeArray(n, dat):
	"""	given n vertices, find the degree of each, that is how many neighbors 
	each one has, from from the list of edge pairs in dat
	look into networkx
	"""
	deg = [0 for i in range(n+1)]

	for i in range(0, len(dat)):
		deg[dat[i][0]] += 1
		deg[dat[i][1]] += 1

	deg.remove(0)
	return " ".join([str(i) for i in deg])

def doubleDegreeArray(n,dat):
	"""returns sum of degrees of each nodes neighbors 
	look into networkx
	"""
	ad_dict = defaultdict(list)

	for i in dat:
		ad_dict[i[0]].append(i[1])
		ad_dict[i[1]].append(i[0])

	edges = [0 for i in range(n+1)]

	for i in range(1, len(edges)):
		for j in ad_dict[i]:
			edges[i] += len(ad_dict[j])

	return edges

def binSearch(alist, item):
    """finds location in sorted list of given item
	"""
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    if found == True: return midpoint + 1 	#if item found, return location
    else: return -1							# else, return -1

    """the solution above is the proper algorithim, but this is the more
    pythonic solution"""
	#try: return alist.index(item) + 1
	#except: return -1
		
def TwoSUM(dat):
	"""
	Given list of integers, outputs indices i and j when the integers there sum 
	to 0, that is where A[i] = -A[j]
	"""
	p = -1
	for i, v in enumerate(dat, start=1):
	 	if -v in dat:
			p = i, dat.index(-v) 
			return p
			
	return p

def ThreeSUM(n,dat):
	"""
	Given list of integers, outputs indices i, j, and z when the integers there 
	sum to 0
	"""
	ori = dat[:]
	dat.sort()
	for i in xrange(n-2):
	    x = dat[i]
	    j = i+1
	    k = n-1
	    while j < k:
	        y = dat[j]
	        z = dat[k]
	        if x+y+z == 0:
	            return sorted([ori.index(x)+1,
	                           ori.index(y)+1,
	                           ori.index(z)+1])
	        elif x+y+z > 0:
	            k = k-1
	        else:
	            j = j+1
	return -1	

def fib(N):
	#return list of Fibonacci Numbers given n
	F = []
	for n in range(N+1):
		if n == 0:
		    F.append(0)
		elif n == 1:
			F.append(1)
		else:
			f = F[n-1] + F[n-2]
			F.append(f)
	return F
