#!/bin/python3
from os import system as sys
from random import randint as lri

def readLine():
    f = open('list.txt')
    l = f.readlines()
    print(l[lri(1, 3)])

readLine()
