#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# calcula a funcao objetivo
def calcula_fo(n, s, d):
    dist_percorrida = 0
    for j in range(0,n-1):
        dist_percorrida += d[s[j]][s[j+1]]
    dist_percorrida += d[s[n-1]][s[0]]
    return dist_percorrida

def calcula_delta(n, s, d, i, j):
    i_antes = i - 1
    i_depois = i + 1
    j_antes = j - 1
    j_depois = j + 1
    if (i == 0):
        i_antes = n-1
    if (i == n-1):
        i_depois = 0
    if (j == 0):
        j_antes = n-1
    if (j == n-1):
        j_depois = 0
    #delta = d[s[i-1]][s[i]] + d[s[i]][s[i+1]] + d[s[j-1]][s[j]] + d[s[j]][s[j+1]]
    return d[s[i_antes]][s[i]] + d[s[i]][s[i_depois]] + d[s[j_antes]][s[j]] + d[s[j]][s[j_depois]]