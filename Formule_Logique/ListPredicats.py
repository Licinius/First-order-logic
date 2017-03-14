from Formule_Logique.Predicat import Predicat
class ListPredicats(object): 
    
    '''
        Ce fichier comprend la liste des predicats que vous voulez ajouter a votre arbre.
    
    '''
    dic = {
     "triangle_1" : Predicat("triangle",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Triangle)),
     "carre_1" : Predicat("carre",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Square)),
     "rond_1" : Predicat("rond",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Circle)),
     "hexagon_1" : Predicat("hexagon",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Hexagon)),
     "circle_1" : Predicat("circle",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Circle)),
     "square_1" : Predicat("square",arite=1,fun=(lambda args: args[1].getIntegerProperty("viewShape")[args[2]] ==args[0].NodeShape.Square)),
     
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