'''
Created on 13 févr. 2017

@author: Marvin
'''
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Constante import Constante
from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Formule import Formule

if __name__ == '__main__':

    pred =  Predicat(2)
    pred.add(Constante.carre)
    pred.add(Constante.triangle)
    pred.add(Constante.rond)
    
    print(pred.get(2))
    print(pred.get(1))
    
    coupleD = Couple(Quantificateur.existe,Constante.triangle)
    coupleG = Couple(Quantificateur.existe,Constante.carre)
    
    form = Formule(coupleD,coupleG,pred)
    print(form)