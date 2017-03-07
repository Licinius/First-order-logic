#-*- coding: utf-8 -*-

from Formule_Logique.Noeud import Noeud



class Noeud_Unaire(Noeud):

    def __init__(self,etiquette,p=None,g=None):
        Noeud.__init__(self, p)
        self.etiquette = etiquette
        self.gauche = g
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
        self.gauche = n
        n.setPere(self)
    #End greffer
    
    def getFilsGauche(self):
        return self.gauche;
    #End getFilsGauche
    '''get le contenu du node'''
    def getEtiquette(self):
        return self.etiquette
    #End getEtiquette
 
    def printFormule(self,p):
        res="\n"
        for i in range(0,p):
            res+="  "
        res +="┖"
        res+='--'
        res+=self.etiquette.__str__()
        #res+=self.couple.__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        