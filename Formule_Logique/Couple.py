'''
Created on 13 févr. 2017

'''
from Formule_Logique import *
class MyClass(object):


        def __init__(self, quant : Quantificateur, at : Atome):
            self.quantificateur = quant
            self.atome = at
        #End Constructor
        
        def getQuantificateur(self):
            return self.quantificateur
        
        def getAtome(self):
            return self.atome
       
       
        