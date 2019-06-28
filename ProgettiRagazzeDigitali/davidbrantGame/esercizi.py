# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:59:38 2019

@author: scr.013
"""

import random

def randomNumber():
    number = random.randint (1, 200)
    return (number) 

number = randomNumber()
print ('il numero è: ' + str(number))



def numberMax(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2
    
numbers = numberMax (15, 180)
print (numbers)

