class UserAlreadyExistsError(Exception):
    def __init__(self, username: str, message='Такой пользователь уже есть в базе'):
        self.username = username
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}: {self.username}'