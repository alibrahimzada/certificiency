

# This is the class handling for requests came through app
class RequestHandler():

    def __init__(self, request):
        self.request = request

    
    def extractContext(self):
        return None

class CoreAppContext:
    user_id = None
    customer_id = None
