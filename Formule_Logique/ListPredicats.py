from Formule_Logique.Predicat import Predicat
class ListPredicats(object): 
    
    '''
        Ce fichier comprend la liste des predicats que vous voulez ajouter a votre arbre.
    
    '''
    dic = {
     "triangle_1" : Predicat("triangle",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Triangle)),
     "carre_1" : Predicat("carre",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Square)),
     "rond_1" : Predicat("rond",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Circle)),
     "hexagon_1" : Predicat("hexagon",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Hexagon)),
     "circle_1" : Predicat("circle",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Circle)),
     "square_1" : Predicat("square",arite=1,fun=(lambda args: graph.getIntegerProperty("viewShape")[args[0]] ==tlp.NodeShape.Square)),
     
     "relier_2" :  Predicat("relier",arite=2,fun=(lambda args : graph.hasEdge(args[0],args[1],False))),
    
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