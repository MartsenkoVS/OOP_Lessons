# library_manager/utils/__init__.py

print('Инициализация подпакета utils')

# Определение списка экспортируемых модулей
__all__ = ['data_validation', 'formatting']

# Импортирование ключевых функций и классов для удобства
from .data_validation import validate_book_data
from .formatting import format_book_data