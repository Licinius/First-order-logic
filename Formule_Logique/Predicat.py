'''
Created on 13 févr. 2017

'''
from Formule_Logique.Constante import Constante

class Predicat(object):

    def __init__(self,n : int):
        self.constantes = []
        self.arite = n
    #End Constructeur
    
    '''
        Ajoute un atome à la fin de la liste si elle n'est pas pleine
    '''
    def add(self,constante : Constante):
        if(len(self.constantes)<self.arite):
            self.constantes.append(constante)
    #End add    
    
    '''
        Retourne l'atome à la n-ième position de la liste.
    '''
    def get(self,i : int):
        if(i<len(self.constantes)):
            return self.constantes[i]
    #End get
    
    def __str__(self):
        retour = "Relier("
        index =0
        for constante in self.constantes:
            if(index==0):
                retour += str(constante.name)
                index+=1
            else:
                retour += "," + str(constante.name)
        return retour+")"
    #End __str__