# library_manager/utils/formatting.py

def format_book_data(data: dict) -> str:
    """
    Форматирует данные книги для вывода в отчет. 
    Пример формата: Title: {title}, Author: {author}, Genre: {genre}.
    """
    data_str = f'Title: {data['Название']}, Author: {data['Автор']}, Genre: {data['Жанр']}'
    return data_str