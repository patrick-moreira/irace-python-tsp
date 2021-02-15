#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from random import randint
from Descida import descida

def ILS(n, s, d, vezesnivel, ILSmax):
    fo, s = descida(n,copy.deepcopy(s),d)
    iteracao = 0
    MelhorIter = 0
    nivel = 1
    while (iteracao - MelhorIter < ILSmax):
        iteracao += 1
        s_2l = copy.deepcopy(s)
        vezes = 0
        while (vezes < vezesnivel):
            ntrocasmax = nivel + 1
            ntrocas = 0
            s_2l = copy.deepcopy(s)
            fo_2l = fo
            while (ntrocas < ntrocasmax):
                ntrocas += 1
                i = randint(0, n-1)
                j = randint(0, n-1)
                while(j == i):
                    j = randint(0, n-1)
                aux = s_2l[i]
                s_2l[i] = s_2l[j]
                s_2l[j] = aux
            
            fo_2l, s_2l = descida(n,copy.deepcopy(s_2l),d)
            if (fo_2l < fo):
                fo = fo_2l
                s = copy.deepcopy(s_2l)
                vezes = 0
                nivel = 1
                MelhorIter = iteracao
            vezes +=1
        nivel += 1
    return fo, s





