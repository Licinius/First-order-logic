from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat


class Noeud_Predicat(Noeud):

    def __init__(self, p : Noeud,c : Predicat):
        Noeud.__init__(self, p)
        self.predicat = c
        self.gauche = None
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n : Noeud):
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
        res+=self.predicat.__str__()
        if(self.gauche is None):
            return res 
        else:
            return res+self.gauche.printFormule(p+1)
        
        