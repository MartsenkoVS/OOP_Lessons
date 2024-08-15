# library_manager/catalog.py

from library_manager.utils.data_validation import validate_book_data

class Library():
    """Класс для управления книгами"""
    def __init__(self):
        self.books = []
        
    def add_book(self, title: str, author: str, genre: str):
        """Добавляет книгу в каталог"""
        book_dict = {'Название': title, 'Автор': author, 'Жанр': genre}
        if validate_book_data(book_dict):
            self.books.append(book_dict)
            print(f'Книга {title} автора {author} добавлена в каталог в жанр {genre}')
        else:
            print('Ошибка в заполнении данных о книге, книга не добавлена в каталог')
        
    def remove_book(self, title: str):
        """Удаляет книгу из каталога по названию""" 
        self.books = [book for book in self.books if book['Название'] != title]
        print(f'Книга {title} удалена из каталога')
        
    def find_book(self, title: str=None, author: str=None, genre: str=None) -> list:
        """Поиск книги по названию, автору и жанру"""
        finded_books = [
            book for book in self.books
            if (title is None or title == book['Название'])
                and (author is None or author == book['Автор'])
                and (genre is None or genre == book['Жанр'])
        ]
        print('По заданным параметрам в каталоге найдены книги:')                             
        return finded_books
    
    def get_all_books(self):
        """Просмотр всех книг в каталоге"""
        print('Список всех книг в каталоге:')
        return self.books