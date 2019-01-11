#!/bin/python3
from random import randint as lri

def readLine():
    f = open('list.txt')
    total = int(sum(1 for line in open('list.txt'))) - 1
    l = f.readlines()
    print(l[lri(1, total)])

readLine()