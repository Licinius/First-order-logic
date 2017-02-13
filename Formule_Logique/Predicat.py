class MyClass(object):

    def __init__(self,n):
        self.atome = []
        self.arite = n
    #End Constructeur
    
    def add(self,Atome):
        if(len(self.atome)<self.arite):
            self.atome.append(Atome)
    #End add    
    
    def get(self,i):
        return self.atome[i]
    