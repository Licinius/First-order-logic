#-*- coding: utf-8 -*-

from Formule_Logique.Noeud import Noeud



class Noeud_Predicat(Noeud):

    def __init__(self, p,c):
        Noeud.__init__(self, p)
        self.predicat = c
        self.gauche = None
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
        self.gauche = n
        n.setPere(self)
    #End greffer
    
    '''get le contenu du node'''
    def getEtiquette(self):
        return self.predicat
    #End getEtiquette
 
    def printFormule(self,p):
        if(p>0):
            res="\n┖"
        else :
            res = ""
        for i in range(0,p):
            res+='--'
        res+=self.predicat.__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        