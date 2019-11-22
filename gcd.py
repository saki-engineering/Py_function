#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

def gcd(A,B):
    if B>A:
        A,B = B,A

    if(A%B==0):
        return B
    else:
        return gcd(B,A%B)