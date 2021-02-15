#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Util import calcula_delta, calcula_fo
from random import randint
import time

def melhor_vizinho(n, s, d, fo):
    fo_melhor_viz = fo
    melhor_i = -1
    melhor_j = -1
    for i in range (0,n-1):
        for j in range(i+1,n):
            # Calcula a variacao de custo com a realizacao do movimento
            delta1 = calcula_delta(n,s,d,i,j)
            # Faz o movimento
            aux = s[j]
            s[j] = s[i]
            s[i] = aux
            delta2 = calcula_delta(n,s,d,i,j)
            # Calcular a nova distancia
            fo_viz = fo - delta1 + delta2            
            # Armazenar o melhor movimento (melhor troca)
            if(fo_viz < fo_melhor_viz):
                melhor_i = i
                melhor_j = j
                fo_melhor_viz = fo_viz
            # Desfaz o movimento
            aux = s[j]
            s[j] = s[i]
            s[i] = aux    
    # retornar a distancia do melhor vizinho
    return fo_melhor_viz, melhor_i, melhor_j

def descida(n, s, d):
    fo = calcula_fo(n, s, d)
    fo_viz = fo
    melhorou = True
    mensagem = ""
    while (melhorou == True):
        melhorou = False
        fo_viz, melhor_i, melhor_j = melhor_vizinho(n, s, d, fo)
        if (fo_viz < fo):
            aux = s[melhor_j]
            s[melhor_j] = s[melhor_i]
            s[melhor_i] = aux

            fo = fo_viz
            melhorou = True
            
    return fo, s

def descida_randomica(n, s, d, IterMax):
    fo = calcula_fo(n,s,d)
    iter = 0
    mensagem = ""
    while (iter < IterMax):
        iter += 1
        j = randint(0,n-1)
        i = randint(0,n-1)
        while(i == j):
            i = randint(0,n-1)
        delta1 = calcula_delta(n,s,d,i,j)
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        delta2 = calcula_delta(n,s,d,i,j)
        fo_viz = fo - delta1 + delta2
        if (fo_viz < fo):
            iter = 0
            fo = fo_viz
        else:
            aux = s[i]
            s[i] = s[j]
            s[j] = aux
    return fo, s