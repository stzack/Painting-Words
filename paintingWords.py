#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from sys import argv
from math import sqrt
from rpy2 import robjects
import math
import os

def fillOccurences(content, occ):
    for symbol in content:
        if symbol in occ:
            occ[symbol] +=1
        else:
            occ[symbol] =  1
    return occ

def parse(argv):
    occ = dict()
    f = open(argv[1])
    size = f.tell()
    for line in f:
        occ = fillOccurences(line, occ)
    return occ

def paint(occ):
    r = robjects.r
    vector = [x for x in occ.values()]
    vector = robjects.FloatVector(vector)
    vector = vector + vector + vector + vector
    row = math.floor(sqrt(len(vector)))
    col = row + 1
    matrix = r.matrix(vector, row, col)
    color = robjects.r("rainbow")(20)
    r.png(filename=os.path.splitext(argv[1])[0]+".png")
    r.image(matrix, axes=False, breaks=robjects.IntVector([0,10,20,30,440,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000]), col=color)
    r('dev.off')()

if __name__ == "__main__":
    if len(argv) > 1:
        paint(parse(argv))
