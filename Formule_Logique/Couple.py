#-*- coding: utf-8 -*-

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
        