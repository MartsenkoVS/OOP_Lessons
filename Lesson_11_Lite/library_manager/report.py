# library_manager/report.py

from library_manager.catalog import Library
from library_manager.utils.formatting import format_book_data

def generate_report(library: Library) -> str:
    """Генерирует отчет о всех книгах в библиотеке в формате строки."""
    report_str = 'Отчет о всех книгах в библиотеке:\n'
    for book in library.books:
        report_str += f'{format_book_data(book)}\n'
    return report_str