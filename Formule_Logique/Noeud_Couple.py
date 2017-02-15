
from Formule_Logique.Noeud import Noeud
from Formule_Logique.Couple import Couple


class Noeud_Couple(Noeud):

    def __init__(self, p,c : Couple):
        Noeud.__init__(self, p)
        self.Couple = c
        self.gauche = None
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n):
        self.gauche = n
        n.setPere(self)
        print("Heritage")
    #End greffer