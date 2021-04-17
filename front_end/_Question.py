

class Question():
    question =""
    answer = 0
    def __init__(self,question):
        self.question = question
        
     
    def get_question(self):
        return self.question
        
    def get_answer(self):
        return self.answer
        
    def __str__(self):
        return "question " + str(self.question) + "answer  " + str(self.answer)
        
    def change_question(self,question):
        self.question = question
    
    def ask_question_get_answer(self,answer):
        self.answer = answer