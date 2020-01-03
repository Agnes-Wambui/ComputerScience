#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:29:07 2018

@author: thejumpingspider
"""

s= 'zyxwvutsrqponmlkjihgfedcba'
l = []
g = []
for i in range (len(s)-1):
    if s[i] <= s[i+1]:
        if i+1  == len(s)-1:
            l.append(s[i])
            l.append(s[i+1])
            g.append(l)
            break
        if s[i+1] > s[i+2]:
            l.append(s[i])
            l.append(s[i+1])
            g.append(l)
            l = []
            continue
        l.append(s[i])
print (g)
if len(g) == 0:
    print ('Longest substring in alphabetical order is:',s[0])
else:
    maxString = max(g , key=len)
    print (maxString)
    print ('Longest substring in alphabetical order is:', ''.join(maxString))

    
        