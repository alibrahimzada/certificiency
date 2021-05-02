
class CustomException(Exception):
    
    def __init__(self, message, isBrutal=False):
        self.message = message
        self.isBrutal = isBrutal
        self.log()

    
    def log(self):
        print(self.message, self.isBrutal)