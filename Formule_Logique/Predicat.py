#-*- coding: utf-8 -*-

class Predicat(object):

    def __init__(self,nom,arite=None,fun=None,listPred=None):
        self.variables = []
        self.nom = nom

        self.function = fun
        
        self.arite = 0
        arr=0
        if(listPred is not None):
            for i in listPred:
                self.variables.append(i)
                arr+=1
            
        if(arite is not None):
            self.arite = arite
        else: 
            self.arite = arr
           
    #End Constructeur
    
    '''
        Ajoute une variable ou atome  à la fin de la liste si elle n'est pas pleine
    '''
    def add(self,variable):
        if(len(self.variables)<self.arite):
            self.variables.append(variable)
    #End add    
    
    def execute(self,tab_parametre):
        return self.function(tab_parametre)
    
    '''
        Retourne la fonction associé au predicat
    '''
    def getFunction(self):
        return self.function;
    
    '''
        Retourne la variable à la n-ième position de la liste.
    '''
    def getVariable(self,i):
        if(i<len(self.variables)):
            return self.variables[i]
    #End get
    
    '''
        Retourne l'arite du predicat
    '''
    def getArite(self):
        return self.arite
    
    def substitution(self,str1,str2):
        index=0;
        for variable in self.variables:
            if(variable==str1):
                self.variables[index] = str2
            index+=1
    #end Substitution
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
    
    def __eq__(self,other):
        if (isinstance(other, Predicat)):
            return((self.nom,self.arite)==(other.nom,other.arite))
        return False