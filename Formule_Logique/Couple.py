'''
Created on 13 févr. 2017

'''
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Constante import Constante


class Couple(object):


        def __init__(self, quant : Quantificateur, c : Constante):
            self.quantificateur = quant
            self.constante = c
        #End Constructor
        
        def getQuantificateur(self):
            return self.quantificateur
        #End getQuantificateur
        
        def getConstante(self):
            return self.constante
        #End getAtome
       
        def __str__(self):
            return str(self.getQuantificateur().name)+" " + str(self.getConstante().name)
        #End __str__
        