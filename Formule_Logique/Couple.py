'''
Created on 13 févr. 2017

'''
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Atome import Atome


class MyClass(object):


        def __init__(self, quant : Quantificateur, at : Atome):
            self.quantificateur = quant
            self.atome = at
        #End Constructor
        
        def getQuantificateur(self):
            return self.quantificateur
        #End getQuantificateur
        
        def getAtome(self):
            return self.atome
        #End getAtome
       
        