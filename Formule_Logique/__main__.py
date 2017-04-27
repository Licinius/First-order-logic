

from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Predicat import Predicat


from Formule_Logique.Noeud_Binaire import Noeud_Binaire
from Formule_Logique.Noeud_Unaire import Noeud_Unaire
from  Formule_Logique.yacc_formuleLogique import parser
from Formule_Logique.Feuille import Feuille
from Formule_Logique.Connecteur_Unaire import Connecteur_Unaire

if __name__ == '__main__':
    c = Couple(Quantificateur.pour_tout,"x")
    N = Noeud_Unaire(etiquette=c)
    c2 = Couple(Quantificateur.existe,"y")
    N2=Noeud_Unaire(etiquette=c2)
    Neg = Noeud_Unaire(etiquette=Connecteur_Unaire.NEG)
    carre = lambda args: args[0] =="carre";
    Carre = Predicat("Carre",1,carre)
    Carre.add("x")
    NP1 = Feuille(Carre)
    N2.greffer(Neg)
    Neg.greffer(N)
    N.greffer(NP1)
    #print(N2)
   # N.remonter()
    #print(N2)
    '''
    
    # Function definition is here
    carre = lambda args: args[0] =="carre";
    rond = lambda args : args[0] == "carre";
    Carre = Predicat("Carre",1,carre)
    Carre.add("x")
    CarreS = Predicat("Carre",1,carre)
    CarreS.add("x")
    
    Rond = Predicat("Rond",1)
    Rond.add("y")
    NP1 = Feuille(Carre)
    NP2 = Feuille(Rond)

   
    NC = Noeud_Binaire(Connecteur.ET)

    NC.greffer(N)
    NC.greffer(N2)
    
    N2.greffer(NP2)

    N.greffer(NP1)
    print(NC)
    '''
    #f = raw_input('Formule : ')
    f = " (Vx carre(x)) > (Vy triangle(y))"
    f= parser.parse(f)
    print(f)
    fres = f.getFilsGauche().remonter()
    print(f.__repr__())
    print(fres.__repr__())
    print(f.racine())
    
    g= parser.parse("carre(x)")
    print(g.negation())
    exit(0)
    
    
