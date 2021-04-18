
from _Question import Question
#from _Saveable import Saveable

class Quiz ():
    quiz_ls = []
    quiz_count = 0 
    def __init__(self,quiz_ls = []):
        super(Quiz,self).__init__()
        self.quiz_ls = quiz_ls
        self.quiz_count = len(self.quiz_ls)
        
    def add_question(self,quest):
        self.quiz_ls.append(self,quest)
        self.quiz_count = len(self.quiz_ls)
        
    def remove_question(self,quest):
        self.quiz_ls.remove(quest)
        self.quiz_count = len(self.quiz_ls)
        
    def __str__(self):
        out = ""
        for i in self.quiz_ls:
            out = out +"|" + str(i) +"|\n"
        return out
        
    def get_data(self):
        save_data = str(self.quiz_count) + ","
        for i in self.quiz_ls:
            save_data = save_data + str(i) + ","
        save_data = save_data + ";\n"
        return save_data