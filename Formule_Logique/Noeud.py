#-*- coding: utf-8 -*-


class Noeud(object):
    
    def __init__(self, etiquete,p=None):
        self.etiquette = etiquete
        self.pere = p
    #End __init_ Noeud
    
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
    
    #Definition de la fonction Greffer dans les fils
                 
    def __str__(self):
        return self.printFormule(0)
    #End _str__