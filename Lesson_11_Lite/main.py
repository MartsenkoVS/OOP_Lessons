# main.py

from library_manager import Library, generate_report

# Инициализируем объект класса Library
library = Library()

# Добавляем книги в каталог
library.add_book(title='Гарри Поттер1', author='Роулинг Дж. К.', genre='Фэнтези')
library.add_book(title='Евгений Онегин', author='Пушкин А.С.', genre='Роман')
library.add_book(title='Капитанская дочка', author='Пушкин А.С.', genre='Роман')
library.add_book(title='Грокаем алгоритмы', author='Бхаргава А.', genre='Обучение')
library.add_book(title='Высоконагруженные приложения', author='Мартин Клеппман', genre='Обучение')
# Попытка добавить книгу с некорректными данными
library.add_book(title=123, author='Неизвестный', genre=0)

# Удаляем книгу из каталога
library.remove_book('Капитанская дочка')

# Поиск книги
print(library.find_book(title='Гарри Поттер1'))
print(library.find_book(genre='Роман'))

# Выводим список всех книг
print(library.get_all_books())

# Формируем отчет
print(generate_report(library))