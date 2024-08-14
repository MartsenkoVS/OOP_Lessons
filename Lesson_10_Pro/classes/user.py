class User():
    """Класс представляющий пользователя"""
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age
        
    def __str__(self):
        return f'Пользователь: (Имя={self.username}, Email={self.email}, Возраст={self.age})'