'''
Created on 13 févr. 2017

@author: Marvin
'''
from Formule_Logique import Couple, Predicat

class MyClass(object):


    def __init__(self, gauche : Couple,droite : Couple, pred : Predicat):
        self.gauche = gauche
        self.droite = droite
        self.predicat = pred
    #End Constructor
    
    def getGauche (self):
        return self.gauche
    #End getGauche
    
    def getDroite (self):
        return self.droite
    #End getDroite
    
    
        