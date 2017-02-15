from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Noeud import Noeud


class Noeud_Connecteur(Noeud):

    def __init__(self, p : Noeud,c : Connecteur):
        Noeud.__init__(self, p)
        self.Connecteur = c
        self.gauche = None
        self.droite =  None
        
    #End __init_ Noeud_Connecteur
    
    '''Si le fils gauche est vide greffe à gauche 
       Si le fils droit est vide greffe à droite
       Sinon greffe à gauche
    '''
    def greffer(self,n : Noeud):
        if(self.gauche is None):
            self.gauche = n
        elif(self.droite is None):
            self.droite = n
        else :
            self.gauche = n
            
        n.setPere(self)
    #End greffer    