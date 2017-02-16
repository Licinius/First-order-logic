'''
Created on 13 févr. 2017

'''
import string

class Predicat(object):

    def __init__(self,nom : string,arite : int):
        self.variables = []
        self.nom = nom
        self.arite = arite
    #End Constructeur
    
    '''
        Ajoute un atome à la fin de la liste si elle n'est pas pleine
    '''
    def add(self,variable):
        if(len(self.variables)<self.arite):
            self.variables.append(variable)
    #End add    
    
    '''
        Retourne l'atome à la n-ième position de la liste.
    '''
    def get(self,i : int):
        if(i<len(self.variables)):
            return self.variables[i]
    #End get
    
    def __str__(self):
        retour = self.nom+"("
        index =0
        for variable in self.variables:
            if(index==0):
                retour += str(variable)
                index+=1
            else:
                retour += "," + str(variable)
        return retour+")"
    #End __str__