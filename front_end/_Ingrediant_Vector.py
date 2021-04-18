import numpy as np
from _Feature import Feature 

class Ingrediant_Vector(Feature):
    vector = np.array([0])
    
    def __init__(self,name = "",vector_ls =[]):
        super(Ingrediant_Vector,self).__init__(name)
        self.vector =  np.array([vector_ls])
        
    def __cmp__(self,other):
        return cmp((self.name,self.vector), (other.name, other.vector))
    
    def __eq__(self,other):
        return self.name == other.name and self.vector == other.vector
    
    def __lt__(self, other):
        return [self.name, self.vector]<[other.name, other.vector]
    
    def __gt__(self,other):
        return [self.name, self.vector]>[other.name, other.vector]
    
    def get_vector(self):
        return self.vector
        
    def __str__(self):
        return str(self.get_vector()) + " " + self.name
    