

class Question():
    question =""
    answer = 0
    idx_map = None
    
    def __init__(self,question,idx_map= None):
        self.question = question
        self.idx_map = idx_map
     
    def get_question(self):
        return self.question
        
    def get_answer(self):
        return self.answer
        
    def __str__(self):
        return "question " + str(self.question) + "answer  " + str(self.answer)
        
    def change_question(self,question):
        self.question = question
        
    def get_idx_map(self):
        return self.idx_map
        
    def ask_question_get_answer(self,answer):
        self.answer = answer