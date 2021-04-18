

class Feature():
    name = None
    value = None
    weight = None
    def __init__(self,name = None,value=None,weight=None):
        self.name = name
        self.value = value
        self.weight = weight
        
    def Modify(self,name,value,weight):
        self.name = name
        self.value = value
        self.weight = weight
    def Get_Name(self):
        return self.name
    def Get_Vale(self):
        return self.val    
    def __eq__(self,other):
        return  isinstance(other, Feature) and self.name == other.name and self.value == other.value and self.weight==other.weight
    
    def __cmp__(self,other):
        return cmp((self.name, self.name,self.weight), (other.name, other.name,other.weight))
    def __lt__(self, other):
        return [self.name, self.name,self.weight]<[other.name, other.name,other.weight]
    def __gt__(self,other):
        return [self.name, self.name,self.weight]>[other.name, other.name,other.weight]
    
    def __name__(self):
        return "feature" + "name "+self.name+" ,val "+str(self.value)+" ,weight "+str(self.weight)+"\n"
    def __str__(self):
        return "name "+self.name+" ,val "+str(self.value)+" ,weight "+str(self.weight)