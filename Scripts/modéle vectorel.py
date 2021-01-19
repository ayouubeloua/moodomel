# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:30:42 2017

@author: hp
"""
import numpy
import string
def vect(list_term_corpus,A):
    list_req0=list()
    req=input("inserer les mots clés séparés par ,")
    list_req0=req.split(',')
    list_req1=list()
    for term in list_term_corpus:
        if term in list_req0:
            list_req1.append(1)
        else:
            list_req1.append(0)
            resultat_ps=list()
            for doc in A:
                r=numpy.array()
                d=numpy.array()
                r=numpy.asarray(list_req1)
                ps=numpy.dot(r,d)
                resultat_ps.append(ps)
######################################
resultat.cos=list()
for doc in A :
 n1=numpy.sqrt((r*r).sum())
 n2=numpy.sqrt((d*d).sum())
 cosin=ps/(n1*n2)
 resultat.cos.append(cosin)
 #########################################
 resultat_jaccard=list()
         for doc in A:
             m1=(r*r).sum()
             m2=(d*d).sum()
             J= ps/(m1+m2-ps)
             resultat_jaccard.append(J)
###########################################"
resultat_dice=list()
    for doc in A:
        k1=r.sum()
        k2=d.sum()
        dice=2*ps/(k1+k2)
        resultat_dice.append(dice)
             
             
 