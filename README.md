# Formule_Logique
# ==============================
Formule logique permet de créer des arbres représentant des formules logique du premier ordre, il contient un parser et des fonctions associées. Il a été créé pour être utilisé avec Tulip afin de générer des graphes. 

### Installation
Pour installer la bibliotèque il suffit de faire : 

```sh
$ python setup.py install
```


### Plugins

| Plugin | Lien |
| ------ | -----|
| Ply | https://pypi.python.org/pypi/ply |
| enum34 | https://pypi.python.org/pypi/enum34 |

L'installation des modules peut se faire à l'aide de pip : 

```sh
$ pip install ply
$ pip install enum34
```
### Syntaxe des formules
* Un prédicat et une variable sont toujours en minuscule et peuvent contenir des caractères  alphanumériques
* Un &and; se traduit par & ou &&
* Un &or; se traduit par | ou ||
* Un &rarr; se traduit par -- , -> , >, >>
* La négation &not;  se traduit par ! ou ~
* Pour les quantificateurs : 
    * &exist; se traduit par E
    * &forall; se traduit par V

### Ajouter des predicats reconnaissable

La démarche d'ajout de prédicat est simple, il suffit de saisir votre fonction python, ensuite de l'ajouter au tableau associatif tel que la clef sera le nom du prédicat suivi d'un sous-tiret et l'arité du prédicat

Exemple : Je veux rajouter le prédicat estChien(x)
1. J'écris la fonction chien qui vérifie si l'argument passé en paramètre est un chien
2. J'ajoute dans tableau associatif une nouvelle ligne telle que :
	dic = {...,"chien_1":Predicat("chien",arite=1,fun=chien)}

Vous n'avez plus qu'à reinstaller le module.

Dans le module ici, les prédicats sont utilisés pour Tulip, ils ont toujours la même forme de fonction, exemple :
```python
 def maFormeIcon(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2] == args[0].NodeShape.maFormeIcon
    else :
        return args[0].NodeShape.maFormeIcon
    ...
    dic = {
    "triangle_1" : Predicat("triangle",arite=1,fun=triangleFunc),
    ..., 
    "maForme_1" : Predicat("maForme",arite=1,fun = maFormeIcon)
    } 
```

Les formes disponibles dans Tulip se trouvent ici :
http://tulip.labri.fr/Documentation/current/tulip-python/html/graphvisualattributes.html#shapes-of-graph-elements

            
