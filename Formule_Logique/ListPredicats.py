from Formule_Logique.Predicat import Predicat
def triangleFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Triangle
    else:
        return args[0].NodeShape.Triangle
#End func 
def starFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Star
    else:
        return args[0].NodeShape.Star
#End func 
def squareFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Square
    else:
        return args[0].NodeShape.Square   

def circleFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Circle
    else:
        return args[0].NodeShape.Circle

def crossFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Cross
    else:
        return args[0].NodeShape.Cross 
    
def diamondFunc(args):
    if(args[1] is not None):
        return args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Diamond
    else:
        return args[0].NodeShape.Diamond 
    
class ListPredicats(object): 
    
 
    '''
        Ce fichier comprend la liste des predicats que vous voulez ajouter a votre arbre.
    
    '''
    dic = {
     "triangle_1" : Predicat("triangle",arite=1,fun=triangleFunc),
     "carre_1" : Predicat("square",arite=1,fun=squareFunc),
     "rond_1" : Predicat("circle",arite=1,fun=circleFunc),
    "circle_1" : Predicat("circle",arite=1,fun=circleFunc),
     "square_1" : Predicat("square",arite=1,fun=squareFunc),
     "cross_1" : Predicat("cross",arite=1,fun=crossFunc),
     "diamond_1" : Predicat("diamond",arite=1,fun=diamondFunc),
     "star_1" : Predicat("star",arite=1,fun=starFunc),
     "etoile_1":Predicat("star",arite=1,fun=starFunc),
     "relier_2" :  Predicat("relier",arite=2,fun=(lambda args : args[0].hasEdge(args[1],args[2],False))),
    
     "exemple_1" : Predicat("exemple",arite=1,fun =(lambda args : True))
    }
    
    '''
        Retourne un dictionaire de predicat d'une arite
    '''
    def getPredicatsArite(self,i):
        list={}
        for key,element in list:
            if(element.getArite()==i):
                list.append(list[key])     
        return list  
    #end func
    
   