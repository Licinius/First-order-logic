#-*- coding: utf-8 -*-

class Noeud(object):
    
    def __init__(self, etiquete,p=None):
        self.etiquette = etiquete
        self.pere = p
    #End __init_ Noeud
    
    def vider(self):
        self.pere = None
    #end vider
    def setPere(self,n):
        self.pere = n
    #End setPere
    
    def getPere (self):
        return self.pere
    #End getPere
    
        '''get le contenu du node'''
    def getEtiquette(self):
        return self.etiquette
    #End getEtiquette
    def racine(self):
        if (self.getPere() is not None):
            return self.getPere().racine()
        else:
            return self
        
    def estFilsGauche(self):
        pere = self.getPere()
        if( pere is not None):
            return self.getEtiquette() == pere.getFilsGauche().getEtiquette()
        return False
    #End estFilsGauche
    
    def estOrphelin(self):
        return self.pere is None
    #Definition de la fonction Greffer dans les fils Noeud_Unaire et Binaire
    
   
    def __str__(self):
        return self.printFormule(0)
    #End _str__