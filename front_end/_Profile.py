from _Saveable import Saveable
from _Profile_Features import Profile_Features
from _Customer_Feature_Profile import Customer_Feature_Profile
from _Ingrediant_Vector import Ingrediant_Vector
class Profile(Saveable):
    user_name = None
    user_password = None
    pf = Customer_Feature_Profile()
    user_ID = None
    def __init__(self,user_name,user_password,pf = Customer_Feature_Profile,user_ID= None):
        super(Profile,self).__init__()
        self.user_name = user_name
        self.user_password = user_password
        self.pf = pf
        self.user_ID = user_ID
        
    def edit_info(self,user_name,user_password,user_ID):
        self.user_name = user_name
        self.user_password = user_password
        self.user_ID = user_ID
        
    def edit_feature_struct(self,pf):
        self.pf = pf
        
    def get_Profile_Features(self):
        return self.pf
        
    def get_vector(self):
        return self.pf.get_vector()
        
    def get_data(self):
        return self.user_name+";" + self.pf.get_data_feat() + self.pf.get_data_quiz()