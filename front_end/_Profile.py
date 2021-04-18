from _Saveable import Saveable
from _Profile_Features import Profile_Features
class Profile(Saveable):
    user_name = None
    user_password = None
    pf = Profile_Features()
    user_ID = None
    def __init__(self,user_name,user_password,pf = None,user_ID= None):
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
        
    def get_data(self):
        return self.user_name+";" + self.pf.get_data_feat() + self.pf.get_data_quiz()