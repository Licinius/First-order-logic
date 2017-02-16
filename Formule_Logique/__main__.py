'''
Created on 13 févr. 2017

@author: Marvin
'''

from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Noeud_Connecteur import Noeud_Connecteur
from Formule_Logique.Noeud_Couple import Noeud_Couple
from Formule_Logique.Noeud_Predicat import Noeud_Predicat

if __name__ == '__main__':
    c = Couple(Quantificateur.pour_tout,"x")
    N = Noeud_Couple(None,c);
    c2 = Couple(Quantificateur.existe,"y")
    N2=Noeud_Couple(None,c2)
    
    # Function definition is here
    carre = lambda arg: arg[0] =="carre";
    
    Carre = Predicat("Carre",1,carre)
    Carre.add("x")

    print(Carre.execute(["carre"]))
    
    Rond = Predicat("Rond",1,None)
    Rond.add("y")
    
    NP1 = Noeud_Predicat(None,Carre)
    NP2 = Noeud_Predicat(None,Rond)
    
    NC = Noeud_Connecteur(None,Connecteur.ET)
    NC.greffer(NP1)
    NC.greffer(NP2)
    
    N2.greffer(NC)
    N.greffer(N2)
    print(N)
    
    
    