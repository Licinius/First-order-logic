#-*- coding: utf-8 -*-
from Formule_Logique.Noeud import Noeud
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Noeud_Exception import Noeud_Binaire_Etiquette
from Formule_Logique.Noeud_Unaire import Noeud_Unaire
import copy

class Noeud_Binaire(Noeud):

    def __init__(self,etiquette,p=None,g=None,d=None):
        if(isinstance(etiquette, Connecteur)):
            Noeud.__init__(self, etiquette, p)
            self.gauche = g
            self.droite =  d
        else :
             raise Noeud_Binaire_Etiquette("L'étiquette d'un noeud binaire doit être un connecteur binaire")
            
        
    #End __init_ Noeud_Connecteur
        
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
    def substitution(self,str1,str2):
        self.gauche.substitution(str1,str2)
        self.droite.substitution(str1,str2)
    #End substitution
    
    def negation(self):
        if(self.etiquette==Connecteur.ET):
            res = Noeud_Binaire(Connecteur.OU)
            res.gauche = self.gauche.negation()
            
        elif(self.etiquette == Connecteur.OU) :
            res = Noeud_Binaire(Connecteur.ET)
            res.gauche = self.gauche.negation()

        elif(self.etiquette == Connecteur.IMP):
            res = Noeud_Binaire(Connecteur.ET)
            res.gauche = copy.deepcopy(self.gauche)
            
        res.droite = self.droite.negation()
        return res       
    def printFormule(self,p):
        res="\n"
        for i in range(0,p):
            res+="  "
        res +="┖"
        res+='--'
        res+=super(Noeud_Binaire, self).getEtiquette().value
        if(self.gauche is None and self.droite is None):
            return res 
        elif(self.gauche is not None and self.droite is None):
            return res+self.gauche.printFormule(p+1)
        elif (self.gauche is None and self.droite is not None):
            return res + self.droite.printFormule(p+1)
        else:
            return res + self.gauche.printFormule(p+1) + self.droite.printFormule(p+1)
        