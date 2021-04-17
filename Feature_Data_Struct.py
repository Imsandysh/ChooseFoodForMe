from Saveable import Saveable
from Feature import Feature

class Feature_Data_Struct(Saveable):
    list_features
    def __init__(self,list_features):
        super.__init__(self,file_location="",indent = 4,sort_keys=True)
        self.list_features =