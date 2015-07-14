#! /Users/dingyang/anaconda/bin/python
from numpy import *
import os,sys
from math import *
sys.setrecursionlimit(10000000)

def merge(L1,L2):
	if L1[-1]<=L2[0]:
		return L1+L2
	else:
		L0=[]
		counter1=0
		counter2=0
		while(counter1<len(L1) and counter2<len(L2)):
			if L1[counter1]<=L2[counter2]:
				L0.append(L1[counter1])
				counter1+=1
			else:
				L0.append(L2[counter2])	
				counter2+=1
		if counter1<len(L1):
			return L0+L1[counter1:]
		elif counter2<len(L2):
			return L0+L2[counter2:]		

def mergesort(L):
	if len(L)==1:
		return L
	middle=len(L)/2
	left=L[:middle]
	right=L[middle:]
	left_sorted=mergesort(left)
	right_sorted=mergesort(right)
	L_sorted=merge(left_sorted,right_sorted)
	return L_sorted	

def main(filename):
	f=open(filename)
	lines=f.readlines()
	L=[]
	for item in lines:
		if len(item.strip())>0:
			L.append(float(item.strip()))	
	f.close()
	L_sorted=mergesort(L)		
	print L_sorted


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print "Usage: %s FILENAME" %  sys.argv[0]
        print "FILENAME is a list of numbers to be sorted, each row has one number."
        sys.exit(1)
    else:
         filename=sys.argv[1]
         main(filename)

