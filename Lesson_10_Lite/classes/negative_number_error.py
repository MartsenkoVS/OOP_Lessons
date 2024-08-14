class Negative_Number_Exception(Exception):
    def __init__(self, number: int, message='Число отрицательное'):
        self.number = number
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}: {self.number}'