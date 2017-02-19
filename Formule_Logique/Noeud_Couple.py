# -*-coding:Latin-1 -*

from Formule_Logique.Noeud import Noeud
from Formule_Logique.Couple import Couple



class Noeud_Couple(Noeud):

    def __init__(self, p,c):
        Noeud.__init__(self, p)
        self.couple = c
        self.gauche = None
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
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
        res+=self.couple.__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        