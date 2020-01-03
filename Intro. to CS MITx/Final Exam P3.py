#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:56:25 2018

@author: thejumpingspider
"""

s = ''
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    s = list(s)
    sCpy = s[:]
    for char in s:
        if char in 'aeiou':
            sCpy.remove(char)
    print (''.join (sCpy))
print (print_without_vowels(s))           