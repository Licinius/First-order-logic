'''
Created on 13 févr. 2017

@author: Marvin
'''
from Formule_Logique.Noeud import Noeud
from Formule_Logique.Noeud_Couple import Noeud_Couple
from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur

if __name__ == '__main__':
    c = Couple(Quantificateur.pour_tout,"x")
    N = Noeud_Couple(None,c);
    N.greffer(N)
    
    
    