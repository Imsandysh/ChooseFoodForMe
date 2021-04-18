from _Feature_Data_Struct import Feature_Data_Struct
from PIL import Image

class Image_Features(Feature_Data_Struct):
    img = Image()
    def __int__(img):
        super(Image_Features,self).__init__()
        self.img = img
        self.extract_data()
    #ToDo add sandeep code  here
    def extract_data():
        
        