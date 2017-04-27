#-*- coding: utf-8 -*-


from Formule_Logique.Connecteur_Unaire import Connecteur_Unaire
import copy
from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Noeud_Exception import Feuille_Etiquette
from Formule_Logique.Noeud_Unaire import Noeud_Unaire

class Feuille(Noeud):

    def __init__(self,etiquette):
        if(isinstance(etiquette, Predicat)):
            Noeud.__init__(self, etiquette)
        else:
            raise Feuille_Etiquette("une feuille d'un arbre de formule possède un predicat en etiquette")
        
    '''Substitue les x par les y '''
    def substitution(self,str1,str2):
        if(isinstance(self.getEtiquette(),Predicat)):
            self.getEtiquette().substitution(str1,str2)
    #End Substitution
    
    '''Retourne la négation de la formule'''
    def negation(self):
        res = Noeud_Unaire(Connecteur_Unaire.NEG)
        res.greffer(copy.deepcopy(self))
        return res
    
    def printFormule(self,p):
        res="\n"
        for i in range(0,p):
            res+="  "
        res +="┖"
        res+='--'
        res+=self.getEtiquette().__str__()
        return res
    
    def __eq__(self,other):
        return self.etiquette == other.etiquette
    #End eq        