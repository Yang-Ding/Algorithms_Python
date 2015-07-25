#! /Users/dingyang/anaconda/bin/python
from numpy import *
import os,sys
from math import *
sys.setrecursionlimit(10000000)

def partition(L,l,r):
	p=L[l]
	i=l
	j=l
	for j in range(l,r+1):	
		if L[j]>=p:
			pass
		else:
			i+=1
			tmp=L[i]
			L[i]=L[j]
			L[j]=tmp
	L[l]=L[i]
	L[i]=p				
	return i 

def quick_sort(L,l,r):
	if l==r:
		return
	elif r==l+1:
		if L[l]>L[r]:
			tmp=L[l]
			L[l]=L[r]
			L[r]=tmp
		return
	else:
		pivot= partition(L,l,r)			
		if pivot==l:
			quick_sort(L,pivot+1,r)
		elif pivot==r:
			quick_sort(L,l,pivot-1)
		else:
			quick_sort(L,l,pivot-1)
			quick_sort(L,pivot+1,r)
	return

def main(filename):
	f=open(filename)
	lines=f.readlines()
	L=[]
	for item in lines:
		if len(item.strip())>0:
			L.append(float(item.strip()))	
	f.close()
	print L
	quick_sort(L,0,len(L)-1) # sort in place		
	print L


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print "Usage: %s FILENAME" %  sys.argv[0]
        print "FILENAME is a list of numbers to be sorted, each row has one number."
        sys.exit(1)
    else:
         filename=sys.argv[1]
         main(filename)

