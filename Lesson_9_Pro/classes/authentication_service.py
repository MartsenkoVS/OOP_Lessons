import uuid
from classes.user import User, Customer, Admin

class AuthenticationService:
    """Сервис для управления регистрацией и аутентификацией пользователей."""
    def __init__(self):
        self.session_tokens = []
        
    def register(self, user_class: str, username: str, email: str, password: str, *args):
        """Регистрация нового пользователя"""
        for user in User.users:
            if user['Пользователь'] == username:
                print('Такой пользователь уже есть в базе, введите другой username')              
        hash_password = User.hash_password(password)
        match user_class:
            case 'Customer':
                print(f'Пользователь {username} успешно зарегистрирован')
                return Customer(username, email, hash_password, args)
            case 'Admin':
                print(f'Администратор {username} успешно зарегистрирован')
                return Admin(username, email, hash_password, args)
            case _:
                print('Такого класса нет в базе, возможные варианты: Customer или Admin')
                    
    def login(self, username: str, password: str):
        """Аутентификация пользователя"""
        for user in User.users:
            if user['Пользователь'] == username:
                hash_password = User.hash_password(password)
                if User.check_password(user['Пароль'], hash_password) is True:
                    # Генерируем токен сессии
                    session_token = str(uuid.uuid4())
                    # Добавляем в список активных пользователей
                    self.session_tokens.append({'Пользователь': username, 'ID': session_token})
                    self.get_current_user()
                    return session_token
                else: 
                    print(f'Введен неверный пароль')
                    return None
        print(f'Пользователя {username} нет в базе')
        return None
                
    def logout(self):
        """Выход пользователя из системы"""
        logout_session = self.session_tokens.pop(-1)
        print(f'Сессия пользователя {logout_session['Пользователь']} завершена')
        
    def get_current_user(self):
        """Возвращает текущего вошедшего пользователя"""
        last_session = self.session_tokens[-1]
        print(f'Пользователь {last_session['Пользователь']} вошел в систему c ID: {last_session['ID']}')