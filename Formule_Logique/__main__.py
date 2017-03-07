

from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Noeud_Binaire import Noeud_Binaire
from Formule_Logique.Noeud_Simple import Noeud_Simple

if __name__ == '__main__':
    c = Couple(Quantificateur.pour_tout,"x")
    N = Noeud_Simple(etiquette=c)
    c2 = Couple(Quantificateur.existe,"y")
    N2=Noeud_Simple(etiquette=c2)
    
    # Function definition is here
    carre = lambda args: args[0] =="carre";
    
    Carre = Predicat("Carre",1,carre)
    Carre.add("x")

    print(Carre.execute(["carre"]))
    
    Rond = Predicat("Rond",1)
    Rond.add("y")
    
    NP1 = Noeud_Simple(Carre)
    NP2 = Noeud_Simple(Rond)
    
    NC = Noeud_Binaire(Connecteur.ET)
    NC.greffer(N)
    NC.greffer(N2)
    
    N2.greffer(NP2)
    N.greffer(NP1)
    print(NC)
    
    ''''f = raw_input('Formule : ')
    # f = "Vx Ey (carre(x) && rond(y)) >> relier(x,y)"
    parser.parse(f)
    exit(0)'''
    
    
