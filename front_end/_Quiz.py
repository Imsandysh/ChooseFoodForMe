
from _Question import Question
from _Saveable import Saveable

class Quiz (Saveable):
    quiz_ls = []
    quiz_count = 0 
    def __init__(self,quiz_ls = []):
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