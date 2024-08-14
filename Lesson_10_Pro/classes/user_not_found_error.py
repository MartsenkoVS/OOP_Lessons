class UserNotFoundError(Exception):
    def __init__(self, username, message='Пользователь не найден в базе'):
        self.username = username
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}: {self.username}'
        
        