# library_manager/__init__.py

# Выполняется при первом импорте пакета
print('Инициализация пакета library_manager')

# Определение списка экспортируемых модулей
__all__ = ['catalog', 'report', 'utils']

# Импортирование ключевых функций и классов для удобства
from .catalog import Library
from .report import generate_report