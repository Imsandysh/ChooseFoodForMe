from _Saveable import Saveable
from _Feature import Feature
import concurrent.futures

class Feature_Data_Struct(Saveable):
    list_features = []
    
    def __init__(self,list_features):
        super(Feature_Data_Struct,self).__init__(file_location="",indent = 4,sort_keys=True)
        self.list_features = list_features
    
    def __eq__(self,other):
        return calc_diff(other) == 0
       
                
    def calc_diff(self,other):
        found = []
        for feat_other in other.list_features:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.check_for,feat_other)
                found.append(future.result())
        return sum(found)
        
    def check_for(self,feat):
        return feat in self.list_features
        
    def sort(self):
        self.list_features.sort()
        
    def __str__(self):
        out = "\n"
        for i in self.list_features:
            out = out +"|" + str(i) +"|\n"
        return out

        