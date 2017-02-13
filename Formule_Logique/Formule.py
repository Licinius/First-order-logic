'''
Created on 13 févr. 2017

@author: Marvin
'''
from Formule_Logique import Couple, Predicat

class Formule(object):


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
    
    def getPredicat (self):
        return self.predicat
    #End getPredicat
    
    def __str__(self):
        return "Formule :" + str(self.getGauche())+" "+ str(self.getDroite()) + " " + str(self.getPredicat())
    #End __str__