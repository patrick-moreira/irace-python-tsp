#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Arquivo import obter_parametros_pcv, le_arq_matriz
from Construcao import constroi_solucao_gulosa_vizinho_mais_proximo, constroi_solucao_aleatoria
from Util import calcula_fo, calcula_delta
from Descida import melhor_vizinho, descida, descida_randomica
from ILS import ILS
import copy
import sys

instancia = sys.argv[1]
for i in range(len(sys.argv)):
    if (sys.argv[i] == "--VEZESNIVEL"):
        vezesnivel = int(sys.argv[i + 1])  
    if (sys.argv[i] == "--ILSMAX"):
        ILSmax = float(sys.argv[i + 1]) 
        
num_cidades = int(instancia.split("_")[1].split(".")[0])
distancia = le_arq_matriz(instancia, num_cidades)

solucao = constroi_solucao_aleatoria(num_cidades)
fo = calcula_fo(num_cidades, solucao, distancia)
fo, s = ILS(num_cidades, copy.deepcopy(solucao), distancia, vezesnivel, ILSmax)
print(fo)
