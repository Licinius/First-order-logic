#-*- coding: utf-8 -*-
from Formule_Logique.Quantificateur import Quantificateur

class Couple(object):


        def __init__(self, quant, c):
            self.quantificateur = quant
            self.variable = c
        #End Constructor
        
        def getQuantificateur(self):
            return self.quantificateur
        #End getQuantificateur
        
        def getVariable(self):
            return self.variable
        #End getVariable
       
        def __str__(self):
            return str(self.getQuantificateur().value)+ self.getVariable()
        #End __str__
        
        def __eq__(self,other):
            if (isinstance(other, Couple)):
                return ((self.quantificateur,self.variable) == (other.quantificateur,other.variable))
            return False
        
            
        def negation(self):
            if(self.quantificateur == Quantificateur.pour_tout):
                self.quantificateur = Quantificateur.existe
            else:
                self.quantificateur = Quantificateur.pour_tout
            
        
        