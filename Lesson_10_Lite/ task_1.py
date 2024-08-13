def connvert_to_int(value: str):
    print(f'В функцию передали аргумент: {value}')
    try:
        int_value = int(value)
    except ValueError as ve:
        print('Ошибка преобразования строки в число')  
        print(f'Тип ошибки: {type(ve).__name__}')
        print(f'Сообщение об ошибке: {ve}')    
    except BaseException as be:
        print('Неожиданная ошибка')
        print(f'Тип ошибки: {type(be).__name__}')
        print(f'Сообщение об ошибке: {be}')
    else:
        print(f'Результат преобразования: {int_value}')     
    finally:
        print('Попытка преобразования завершена\n')


connvert_to_int('123')
connvert_to_int('abc')
connvert_to_int([1, 2, 3])

