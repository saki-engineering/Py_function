#coding: utf-8
import math
import heapq

MOD = 10**9+7

def combination(n, r):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD-2, MOD) % MOD
