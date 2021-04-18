from _Feature_Data_Struct import Feature_Data_Struct
from _Ingrediant_Vector import Ingrediant_Vector
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from numpy.linalg import norm
import math

class Menu_Matrix(Feature_Data_Struct):
    #naming 
    menu = np.matrix([[0,0],[0,0]])
    comperator = Ingrediant_Vector([1]) #optional if you want to sort
    
    def __init__(self,list_features = []):
        super(Menu_Matrix,self).__init__(list_features)
        
        self.menu = np.matrix(self.list_features[0].get_vector())
        for i in range(1,len(self.list_features)):
            #print("men\n",self.menu )
            #print("vect\n",self.list_features[i].get_vector())
            self.menu = np.concatenate((self.menu,self.list_features[i].get_vector()))
            #self.menu = np.append([self.menu],[i.get_vector()])
    
    def angle_similarity_vect(self,other):
        other = other
        #return np.dot(self.menu,other)/(norm(self.menu)*norm(other.T))
        cosine_similarity = linear_kernel(self.get_menu(),other)
        print(cosine_similarity)
        return cosine_similarity
        
    def get_close_recomendation(self,other):
        angle_vector = self.angle_similarity_vect(other.get_vector())
        return self.list_features[np.argmax(angle_vector)].name
        
    def get_far_recomendation(self,other):
        angle_vector = self.angle_similarity_vect(other.get_vector())
        return self.list_features[np.argmin(angle_vector)].name
        
    def get_menu(self):
        return self.menu
        
    def __eq__(self,other):
        return self.get_menu() == other.get_menu()
        
    def __lt__(self,other):
        this_angle_vector = self.angle_similarity_vect(comperator)
        other_angle_vector = self.angle_similarity_vect(comperator)
        return norm(this_angle_vector) < norm(other_angle_vector)
        
    def __gt__(self,other):
        this_angle_vector = self.angle_similarity_vect(comperator)
        other_angle_vector = self.angle_similarity_vect(comperator)
        return norm(this_angle_vector) > norm(other_angle_vector)
        
    def __str__(self):
        return str(self.get_menu()) + str(self.list_features)