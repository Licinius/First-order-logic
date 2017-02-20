#-*- coding: utf-8 -*-
from Formule_Logique.Noeud import Noeud


class Noeud_Connecteur(Noeud):

    def __init__(self, p,c):
        Noeud.__init__(self, p)
        self.Connecteur = c
        self.gauche = None
        self.droite =  None
        
    #End __init_ Noeud_Connecteur
    
    '''get le contenu du node'''
    def getEtiquette(self):
        return self.Connecteur
    #End getEtiquette
    
    def getFilsGauche(self):
        return self.gauche;
    #End getFilsGauche
    '''Si le fils gauche est vide greffe à gauche 
       Si le fils droit est vide greffe à droite
       Sinon greffe à gauche
    '''
    def greffer(self,n):
        if(self.gauche is None):
            self.gauche = n
        elif(self.droite is None):
            self.droite = n
        else :
            self.gauche = n
            
        n.setPere(self)
    #End greffer    
        
    def printFormule(self,p):
        if(p>0):
            res="\n┖"
        else :
            res = ""
        for i in range(0,p):
            res+='--'
        res+=self.Connecteur.value
        if(self.gauche is None and self.droite is None):
            return res 
        elif(self.gauche is not None and self.droite is None):
            return res+self.gauche.printFormule(p+1)
        elif (self.gauche is None and self.droite is not None):
            return res + self.droite.printFormule(p+1)
        else:
            return res + self.gauche.printFormule(p+1) + self.droite.printFormule(p+1)
        