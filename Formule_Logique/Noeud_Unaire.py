#-*- coding: utf-8 -*-

from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat


class Noeud_Unaire(Noeud):

    def __init__(self,etiquette,p=None,g=None):
        Noeud.__init__(self,etiquette, p)
        self.gauche = g
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
        self.gauche = n
        n.setPere(self)
    #End greffer
    
    def getFilsGauche(self):
        return self.gauche;
    #End getFilsGauche
    
    '''Substitue les x par les y '''
    def substitution(self,str1,str2):
        if(isinstance(self.getEtiquette(),Predicat)):
            self.getEtiquette().substitution(str1,str2)
        if(self.gauche is not None):
            self.gauche.substitution(str1,str2)
          
 
    def printFormule(self,p):
        res="\n"
        for i in range(0,p):
            res+="  "
        res +="┖"
        res+='--'
        res+=super(Noeud_Unaire, self).getEtiquette().__str__()
        #res+=self.couple.__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        