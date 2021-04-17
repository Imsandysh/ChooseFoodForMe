class Saveable():
    file_location
    data
   def __init__(self,file_location="",indent = 4,sort_keys=True):
        self.file_location = file_location
        self.indent = indent
        self.sort_keys = sort_keys
    
    #expects a dict
    def input_data(self,data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def Save(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=self.sort_keys, indent=self.indent)