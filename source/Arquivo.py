#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
import numpy as np

# le um arquivo no formato "numero_cidades melhor_fo_literatura"
def obter_parametros_pcv(nomearq):
    try:
        arquivo = open(nomearq, 'r')
    except OSError:
        print("O arquivo", nomearq, "não pode ser aberto")
        sys.exit()
    num_cidades, melhor_fo_literatura = arquivo.readline().split(" ")
    arquivo.close()
    return num_cidades, melhor_fo_literatura


#le um arquivo no formato num_cid coord_x coord_y e calcula as distancias d_ij
def le_arq_matriz(nomearq, n):
    try:
        arquivo = open(nomearq, 'r')
    except OSError:
        print("O arquivo", nomearq, "não pode ser aberto")
        sys.exit()
    vet_x = []
    vet_y = []
    for linha in arquivo:
        i, x, y = linha.split(" ")
        vet_x.append(int(x))
        vet_y.append(int(y))
    # gera a matriz de distancias calculado a partir das distancias euclidianas dos pontos
    distancia = np.zeros((n,n))
    for i in range(0,n):
        for j in range(i+1,n):
            distancia[i][j] = math.sqrt(pow(vet_x[i] - vet_x[j],2) + pow(vet_y[i] - vet_y[j],2))
            distancia[j][i] = distancia[i][j];        
    arquivo.close()
    return distancia 