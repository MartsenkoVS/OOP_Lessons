class Negative_Number_Exception(Exception):
    def __init__(self, number: int, message='Число отрицательное'):
        super().__init__(message)
        self.number = number
        self.message = message
        
    def __str__(self):
        return f'{self.message}: {self.number}'