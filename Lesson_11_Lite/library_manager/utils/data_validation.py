# library_manager/utils/data_validation.py

def validate_book_data(data: dict) -> bool:
    """
    Проверяет корректность данных книги.
    Проверяет, что все обязательные поля присутствуют и корректны.
    """
    return ('Название' in data and isinstance(data['Название'], str)
        and 'Автор' in data and isinstance(data['Автор'], str) 
        and 'Жанр' in data and isinstance(data['Жанр'], str))