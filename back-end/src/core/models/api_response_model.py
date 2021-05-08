

class ApiResponseModel:

    def __init__(self, status, code):
        self.status = status    # Status (Boolean)
        self.code = code    # HTTP Code 200 - Success Code