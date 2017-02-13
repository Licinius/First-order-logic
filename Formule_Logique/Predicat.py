'''
Created on 13 févr. 2017

'''
from Formule_Logique import *
class MyClass(object):

    def __init__(self,n : int):
        self.atome = []
        self.arite = n
    #End Constructeur
    
    '''
        Ajoute un atome à la fin de la liste si elle n'est pas pleine
    '''
    def add(self,atome : Atome):
        if(len(self.atome)<self.arite):
            self.atome.append(atome)
    #End add    
    
    '''
        Retourne l'atome à la n-ième position de la liste.
    '''
    def get(self,i : int):
        return self.atome[i]
    #End get