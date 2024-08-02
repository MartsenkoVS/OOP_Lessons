from classes.user import User, Customer, Admin
from classes.authentication_service import AuthenticationService

# Инициализируем экземпляр класса AuthenticationService
auth_service = AuthenticationService()

# Регистрируем пользователя и администратора
auth_service.register('Customer', 'Martsenko', 'martsenko@gmail.com', '12345678', 'Moscow')
auth_service.register('Admin', 'admin', 'admin@gmail.com', '87654321', 5)

# Аутентификация пользователя
auth_service.login('Martsenko', '12345678')

# Выход пользователя
auth_service.logout()

# Просмотр пользователей
print(Admin.list_users())

# Удаление пользователя
Admin.delete_user('Martsenko')
print(Admin.list_users())