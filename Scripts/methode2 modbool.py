# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:33:26 2017

@author: hp
"""

une méthode qui demande de saisir la req 
des mots clés pr trouver les docs pertinents
continu=true
liste_req=list()
while continu==true
    r1=input('donner le terme')
    liste_req.append(r1)
    existe=input('le terme doit apparaitre ou non:Y/N')
    liste_req.append(existe)
    ajout=input('voulez-vous ajouter dautres termes:Y/N')
    if ajout=='Y':
        opr=input('inserer lopérateur OR/AND')
        liste_req.append(opr)
    else:
        continu=false
    

    
