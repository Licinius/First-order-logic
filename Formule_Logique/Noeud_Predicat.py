from Formule_Logique.Noeud import Noeud
from Formule_Logique.Predicat import Predicat


class Noeud_Couple(Noeud):

    def __init__(self, p : Noeud,c : Predicat):
        Noeud.__init__(self, p)
        self.predicat = c
        self.gauche = None
        
    #End __init_ Noeud_Connecteur

    def greffer(self,n : Noeud):
        self.gauche = n
        n.setPere(self)
    #End greffer