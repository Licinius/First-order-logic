#-*- coding: utf-8 -*-
from Formule_Logique.Noeud import Noeud


class Noeud_Binaire(Noeud):

    def __init__(self,etiquette,p=None,g=None,d=None):
        Noeud.__init__(self, p)
        self.Connecteur = etiquette
        self.gauche = g
        self.droite =  d
        
    #End __init_ Noeud_Connecteur
    
    '''get le contenu du node'''
    def getEtiquette(self):
        return self.Connecteur
    #End getEtiquette
    
    def getFilsGauche(self):
        return self.gauche;
    #End getFilsGauche
    
    def getFilsDroit(self):
        return self.droite;
    #End getFilsDroit
    
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
        res="\n"
        for i in range(0,p):
            res+="  "
        res +="┖"
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
        