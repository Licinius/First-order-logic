#-*- coding: utf-8 -*-

from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Noeud_Exception import Noeud_Unaire_Etiquette
from Formule_Logique.Couple import Couple
from Formule_Logique.Connecteur_Unaire import Connecteur_Unaire
import copy


class Noeud_Unaire(Noeud):

    def __init__(self,etiquette,p=None,g=None):
        if(not isinstance(etiquette, Connecteur)):
            Noeud.__init__(self,etiquette, p)
            self.gauche = g
        else:
            raise Noeud_Unaire_Etiquette("L'étiquette d'un noeud unaire ne doit pas être un Connecteur Binaire")
        
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
    
    def negation(self):
        if(self.etiquette==Connecteur_Unaire.NEG):
            if(self.gauche is not None):
                res = copy.deepcopy(self.gauche)
        
        elif(isinstance(self.etiquette,Couple)): 
            res=Noeud_Unaire((self.etiquette.negation()))
            if(self.gauche is not None):
                res.gauche = self.gauche.negation()
        else:
            res = Noeud_Unaire(Connecteur_Unaire.NEG)
            res.gauche = copy.deepcopy(self)
        return res
    #End negation
    
    def __eq__(self,other):
        return ((self.etiquette,self.gauche) == (other.etiquette,other.gauche))
    #End eq      
       
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
        
        