#-*- coding: utf-8 -*-

from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Noeud_Exception import Noeud_Unaire_Etiquette,\
    filsAbsentRemonter
from Formule_Logique.Couple import Couple
from Formule_Logique.Connecteur_Unaire import Connecteur_Unaire
import copy


class Noeud_Unaire(Noeud):

    def __init__(self,etiquette,p=None,g=None):
        if(not isinstance(etiquette, Connecteur) and (not isinstance(etiquette,Predicat))):
            Noeud.__init__(self,etiquette, p)            
            self.gauche = g
            if(g is not None):
                self.gauche.setPere(self)
        else:
            raise Noeud_Unaire_Etiquette("L'étiquette d'un noeud unaire ne doit pas être un Connecteur Binaire ni un Predicat")
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
        self.gauche = n
        if(self.gauche is not None):
            self.gauche.setPere(self)
    #End greffer
    
    def vider(self):
        self.gauche = None
    #end vider
    
    ''' Remonter permet de faire remonter un quantificateur dans l'arbre tant qu'il y a des connecteur binaire'''
    def remonter(self):
        if (self.gauche is None):
            raise filsAbsentRemonter("Le quantificateur n'avait pas de fils lors de la remonter")
        
        if(isinstance(self.etiquette, Couple)):
            if(self.getPere() is not None):
                if(not isinstance(self.getPere(),Couple)):
                    etiquettePere = self.getPere().getEtiquette()
                    if(etiquettePere == Connecteur_Unaire.NEG):
                        self.getEtiquette().negation()
                    if(etiquettePere == Connecteur.IMP):
                        if(self.estFilsGauche()):
                            self.getEtiquette().negation()
                            
                    
                    if(self.estFilsGauche()):
                        self.getPere().grefferFilsGauche(self.gauche)
                    else :
                        self.getPere().grefferFilsDroit(self.gauche)
                    pereEtaitOrphelin = False
                    
                    if(self.getPere().estFilsGauche()):
                        self.getPere().getPere().grefferFilsGauche(self)
                    elif(self.getPere().estOrphelin()):
                        pereEtaitOrphelin = True
                    else:
                        self.getPere().getPere().grefferFilsDroit(self)

                    self.grefferFilsGauche(self.gauche.getPere())
                    if(pereEtaitOrphelin):
                        self.setPere(None)
        return self
    #end remplacerPourLePerePar
        
    
    def grefferFilsGauche(self,n):
        self.gauche = n
        n.setPere(self)
    #End grefferG
    
    def getFilsGauche(self):
        return self.gauche;
    #End getFilsGauche
    
    '''Substitue les x par les y '''
    def substitution(self,str1,str2):
        if(self.gauche is not None):
            self.gauche.substitution(str1,str2)
    
    def negation(self):
        if(self.etiquette==Connecteur_Unaire.NEG):
            if(self.gauche is not None):
                res = copy.deepcopy(self.gauche)
        else: #c'est un couple
            res=Noeud_Unaire((self.etiquette.negation()))
            if(self.gauche is not None):
                res.gauche = copy.deepcopy(self.gauche).negation()
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
        res+=self.getEtiquette().__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        