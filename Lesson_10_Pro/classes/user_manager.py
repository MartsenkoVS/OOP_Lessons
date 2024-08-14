from classes.user import User
from classes.user_already_exists_error import UserAlreadyExistsError
from classes.user_not_found_error import UserNotFoundError

class UserManager():
    """
    Менеджер пользователей, позволяет добавлять, удалять и находить пользователей.
    """
    def __init__(self, users: dict):
        self.users = users
        
    def add_user(self, user: User):
        """Добавляет пользователя"""
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        else:
            self.users[user.username] = user
            print(f'Пользователь {user.username} добавлен в базу')
            
    def remove_user(self, username: str):
        """Удаляет пользователя"""
        if username not in self.users:
            raise UserNotFoundError(username)
        else:
            self.users.pop(username)
            print(f'Пользователь {username} удален из базы')
            
    def find_user(self, username: str) -> User:
        """"Возвращает пользователя по имени"""
        if username not in self.users:
            raise UserNotFoundError(username)
        else:
            return self.users[username]