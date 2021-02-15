#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from random import randint

# Constroi uma solucao gulosa pelo metodo do vizinho mais proximo
def constroi_solucao_gulosa_vizinho_mais_proximo(n, d):
    s = [0]                  # cidade de origem
    nao_visitada = []
    for x in range(1,n):
        nao_visitada.append(x)      # cidades candidatas
    # Partindo da solução cidade 1, constroi uma heurística gulosa buscando, em cada etapa, 
    #a cidade mais próxima que ainda não foi visitada
    while (len(nao_visitada) > 0):
        d_ultima = d[s[len(s)-1]]
        menor_distancia = float('inf')     #numero infinito 
        proxima_cidade = -1
        # Procura qual a cidade mais próxima que ainda não foi visitada
        for x in range(0, len(d_ultima)): 
            if (d_ultima[x] < menor_distancia and d_ultima[x] != 0 and x in nao_visitada):
                menor_distancia = d_ultima[x]
                proxima_cidade = x
        s.append(proxima_cidade)
        nao_visitada.remove(proxima_cidade)
    return s

# Constroi uma solucao de forma aleatoria
def constroi_solucao_aleatoria(n):
    s = []    
    C = []
    for x in range(0,n):
        C.append(x)      # cidades candidatas
    while (len(C) > 0):
        # sorteia a posicao da cidade escolhida
        posicao = randint(0, len(C)-1)
        s.append(C[posicao])
        C.remove(C[posicao])
    return s

