class GOFException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.message)
