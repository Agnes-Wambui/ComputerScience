#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:23:17 2018

@author: thejumpingspider
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Professor.say(self, stuff) 
    def lecture(self, stuff):         
        return 'It is obvious that ' + Person.say(self, stuff)  

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')
print (le.lecture("I'm the smartest. "))
print (pe.say("I'm the smartest. "))
print (ae.say("I'm the smartest. "))
print (ae.lecture("I'm the smartest. "))