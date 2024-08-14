from classes.user import User
from classes.user_manager import UserManager
from classes.user_already_exists_error import UserAlreadyExistsError
from classes.user_not_found_error import UserNotFoundError

# Инициализируем объект класса UserManager
user_manager = UserManager({})

# Создаем пользователей
user_1 = User(username='vit', email='m@mail.ru', age=32)
user_2 = User(username='vita', email='ma@mail.ru', age=32)
user_3 = user_1

# Добавляем пользователя в словарь
user_manager.add_user(user_1)
user_manager.add_user(user_2)
# Обработка исключения для повторного пользователя
try:
    user_manager.add_user(user_3)
except UserAlreadyExistsError as uaee:
    print(uaee)
    
# Удаляем пользователя
user_manager.remove_user('vita')
# Обработка исключения для несуществующего пользователя
try:
    user_manager.remove_user('aaaa')
except UserNotFoundError as unfe:
    print(unfe)
    
#Ищем пользователя
user_manager.find_user('vit')
# Обработка исключения для несуществующего пользователя
try:
    user_manager.find_user('aaa')
except UserNotFoundError as unfe:
    print(unfe)