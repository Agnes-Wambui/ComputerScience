#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:34:33 2018

@author: thejumpingspider
"""
aDict = {}
#aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} 
#aDict = {1: 1, 2: 1, 3: 1}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    rDict = {}
    l = []
    m= []
    vals = list(aDict.values())
    kys = list(aDict.keys())
    for i in range(len(aDict)):
        if vals[i] in rDict:
            rDict[vals[i]].append(kys[i])
        else:
            rDict[vals[i]] = [kys[i]]
    for j in list(rDict.keys()):
      if len(rDict[j]) == 1:
           l.append((rDict[j]))
    for k in l:
        for n in k:
            m.append(n)
    return (sorted(m))
    
        
print (uniqueValues(aDict))  