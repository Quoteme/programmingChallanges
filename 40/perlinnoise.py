#!/usr/bin/env python3
import random
import functools as ft

import matplotlib.pyplot as plt
import math
import numpy as np
import numpy.linalg as la

def gradientvector(n):
        """
        Returns a random gradient vector of dimension n
        """
        v = np.array([random.random()*2-1 for _ in range(n)])
        return v/la.norm(v)

def perlin(g=[10,10],dg=[5,5],interpolation=5):
    """
    Returns an array of n dimensions containing perlin noise.

    n is the length of g, which is the same as dg
    g is the amount of random elements chosen per basisvector
    dg is the amount of elements between each random element
    interpolation determines how many times the perlin noise will be interpolated

    g*dg is the total size of the outcoming perlin noise array.
    """
    # GRID of random gradientvectors
    grid = np.random.random(g+[len(g)])*2 - np.ones(g+[len(g)])
    # normalize grid vectors
    for e in np.ndenumerate(grid):
        p = e[0][:-1]
        v = grid[p]
        grid[tuple(p)] = v/la.norm(v)
    # array that stores perlin noise
    arr = np.zeros( np.multiply(g,dg) )
    # calculate entries of perlin nose array
    for e in np.ndenumerate(arr):
        pos                   = e[0]
        nex                   = [math.floor(pos[i]/dg[i]) for i in range(len(pos))]
        relativePosition      = np.array(pos)-np.array(nex)*np.array(dg)
        nearestGradientVector = grid[tuple(nex)]
        # print(nearestGradientVector)
        arr.itemset(tuple(pos), np.dot(relativePosition,nearestGradientVector))
        # arr.itemset(pos, random.random())
    # interpolate perlin noise array
    for _ in range(interpolation):
        arr = interpolate(arr)
    return arr

    # noise = ft.reduce(lambda x,y: [x for _ in range(y[0]*y[1])], zip(g,dg), None)
    # DOT-PRODUCT
    # def traverseMultidimensionalArray(callback,p=[0 for _ in g], i=0):
    #     """
    #     given an array with n natural numbers inside, apply callback on
    #     all combinations of arrays that are smaller or equal in length
    #     """
    #     callback(p)
    #     try:
    #         if p[i] < g[i]:
    #             q = list(p)
    #             q[i] += 1
    #             traverseMultidimensionalArray(callback,p,i+1)
    #             traverseMultidimensionalArray(callback,q,i)
    #             traverseMultidimensionalArray(callback,q,i+1)
    #     except:
    #         return
    # print(traverseMultidimensionalArray(lambda))

    # return noise

# # grid :: [Integer] -> Integer*[ Integer*[] ]
# def grid(g,n=None):
#     if n == None:
#         n = len(g)
#     if len(g) > 1:
#         return [ grid(g[1:],n) for _ in range(g[0])]
#     elif len(g) == 1:
#         return [ vector(n) for _ in range(g[0]) ]

# def vector(n):
#     return [ random.random() for _ in range(n)]

def interpolate(arr,f=(lambda x,y: (x+y)/2) ):
    for e in np.ndenumerate(arr):
        for d in range(len(e[0])):
            try:
                p = list(e[0])
                p[d] -= 1
                arr[e[0]] = f( arr[e[0]],arr[tuple(p)])
            except:
                None
            try:
                p = list(e[0])
                p[d] -= 1
                arr[e[0]] = f( arr[e[0]],arr[tuple(p)])
            except:
                None
    return arr

def main():
    a = perlin([10,10],[20,20])
    plt.matshow(a)
    plt.savefig('mygraph.png')

if __name__ == "__main__":
    main()
