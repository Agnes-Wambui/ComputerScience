#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:29:57 2018

@author: thejumpingspider
"""

def genPrimes():
    p= [2]
    num =3
    yield 2
    while True:
        q = []
        for i in p:
            q.append(num%i)
        if 0 not in q:
            yield num
            p.append(num)
        num +=1

#p= [2]
#    #yield 2
#for num in range (3,50):
#    q = []
#    for i in p:
#        q.append(num%i)
#    if 0 not in q:
#           # yield num
#        p.append(num)
#print (p)