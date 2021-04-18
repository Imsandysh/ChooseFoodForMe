

from _Feature_Data_Struct import Feature_Data_Struct
from _Quiz import Quiz

class Customer_Feature_Profile(Feature_Data_Struct):
    question_count = 0
    quiz = Quiz()
    
    def __init__(self,list_features= [],quiz = Quiz()):
        super(Profile_Features,self).__init__(list_features)
        self.quiz = quiz
        self.question_count = self.quiz.quiz_count
    
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