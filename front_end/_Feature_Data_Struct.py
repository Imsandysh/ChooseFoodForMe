from _Saveable import Saveable
from _Feature import Feature
import concurrent.futures

class Feature_Data_Struct(Saveable):
    list_features = []
    
    def __init__(self,list_features):
        super(Feature_Data_Struct,self).__init__(file_location="",indent = 4,sort_keys=True)
        self.list_features = list_features
    def Get_Feat_idx(self,idx):
        return self.list_features[idx]
    def __eq__(self,other):
        return self.calc_diff(other) == 0
       
                
    def calc_diff(self,other):
        self.sort()
        other.sort()
        found = []
        for i in range(0,len(self.list_features),1):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                print(other.Get_Feat_idx(i))
                future = executor.submit(self.check_for,other.Get_Feat_idx(i),self.Get_Feat_idx(i))
                found.append(future.result())
        print(sum(found))
        return sum(found)-len(self.list_features)
        
    def check_for(self,feat1,feat2):
        return  feat1 == feat2
        
    def sort(self):
        self.list_features.sort()
        
    def __str__(self):
        out = "\n"
        for i in self.list_features:
            out = out +"|" + str(i) +"|\n"
        return out

        