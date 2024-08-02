import hashlib

class User():
    """Базовый класс представляющий пользователя."""
    users = [] # Список для хранения всех пользователей
    
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        User.users.append({'Пользователь': self.username, 'Email': self.email, 'Пароль': self.password})
        
    @staticmethod
    def hash_password(password: str):
        """Хеширование пароля"""
        # Конвертируем строку в байты
        byte_password = password.encode()
        # Создаем объект хеша
        hash_object = hashlib.sha256(byte_password)
        # Получаем хеш в шестнадцатеричном формате
        hash_password = hash_object.hexdigest()
        return hash_password
    
    @staticmethod
    def check_password(stored_password: str, provided_password: str):
        """Проверка пароля"""
        if stored_password == provided_password: return True         
        else: return False
        
    def get_details(self):
        return f'Пользователь: {self.username}, Email: {self.email}'


class Customer(User):
    """Класс, представляющий клиента, наследующий класс User."""
    def __init__(self, username: str, email: str, password: str, address: str):
        super().__init__(username, email, password)
        self.address = address
        
    def get_details(self):
        return f'Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}'
    

class Admin(User):
    """Класс, представляющий администратора, наследующий класс User."""
    def __init__(self, username: str, email: str, password: str, admin_level: int):
        super().__init__(username, email, password)
        self.admin_level = admin_level
        
    def get_details(self):
        return f'Администратор: {self.username}, Email: {self.email}, Уровень доступа: {self.admin_level}'
    
    @staticmethod
    def list_users():
        """Выводит список всех пользователей"""
        return f'Список всех пользователей: {User.users}'
        
    @staticmethod
    def delete_user(username: str):
        """Удаляет пользователя по имени пользователя"""
        User.users = [user for user in User.users if user['Пользователь'] != username]
        print(f'Пользователь {username} удален из базы')