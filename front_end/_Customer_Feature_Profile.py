

from _Profile_Features import Profile_Features
from _Ingrediant_Vector import Ingrediant_Vector
from _Quiz import Quiz

class Customer_Feature_Profile(Profile_Features):
    question_count = 0
    quiz = Quiz()
    prof_vector = Ingrediant_Vector()
    def __init__(self,prof_vector=Ingrediant_Vector() ,quiz = Quiz()):
        super(Customer_Feature_Profile,self).__init__()
        self.quiz = quiz
        self.question_count = self.quiz.quiz_count
        self.prof_vector = prof_vector
        
        self.map_question_vector()
    
    def map_question_vector(self):
       
        for i in self.quiz.get_quiz_ls():
            print(i.get_idx_map(),i.get_answer())
            self.prof_vector.set_idx(i.get_idx_map(),i.get_answer())
            
    def get_vector(self):
        return self.prof_vector
        
    def add_quest(self,quest):
        self.quiz.append(quest)
        self.quiz = len(self.quiz)
        
    def rm_quest(self,quest):
        self.quiz.remove(quest)
        self.quiz = len(self.quiz)
        
    def get_question_count(self):
        return self.question_count
        
    def __str__(self):
        out = "\n"
        for i in self.list_features:
            out = out +"|" + str(i) +"|\n"
        out = out + ("----------------------------\n")    
        out = out + str(self.quiz)
        out = out +  "question_count " + str( self.get_question_count()) + "\n"
        return out + "feature_count " + str( self.get_feature_count())
    
    def get_data_quiz(self):
        return self.quiz.get_data()