#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:18:59 2018

@author: thejumpingspider
"""
L=[]
#L = [5, 4, 10]
#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    dec = []
    bigDec = []
    inc = []
    bigInc = [] 
    for i in range (len(L)-1):
        if L[i] <= L[i+1]:
            if i+1 == len(L)-1:
                inc.append(L[i])
                inc.append(L[i+1])
                bigInc.append(inc)
                break
            if L[i+1] > L[i+2]:
                inc.append(L[i])
                inc.append(L[i+1])
                bigInc.append(inc)
                inc = []
                continue
            inc.append(L[i])
        if L[i] >= L[i+1]:
            if i+1 == len(L)-1:
                dec.append(L[i])
                dec.append(L[i+1])
                bigDec.append(dec)
                break
            if L[i+1] < L[i+2]:
                dec.append(L[i])
                dec.append(L[i+1])
                bigDec.append(dec)
                dec = []
                continue
            dec.append(L[i])
    
    if bigInc != [] and bigDec != []:
        maxInc = max(bigInc, key=len)
        maxDec = max(bigDec, key=len)
        if len(maxInc) > len(maxDec):
            return sum(maxInc)
        elif len(maxDec) > len(maxInc):
            return sum(maxDec)
        else:
            if L.index(maxInc[0]) <= L.index(maxDec[0]):
                return sum(maxInc)
            else:
                return sum(maxDec)
    elif bigInc != [] and bigDec == []:
        maxInc = max(bigInc, key=len)
        return sum(maxInc)
    elif bigInc == [] and bigDec != []:
        maxDec = max(bigDec, key=len)
        return sum(maxDec)      
        
    
print (longest_run(L))  
        
    