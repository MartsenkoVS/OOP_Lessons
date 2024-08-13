def validate_user_input(data: dict):
    print(f'В функцию передали аргумент: {data}')
    try:
        if not isinstance(data, dict):
            raise TypeError('Ошибка: Аргумент data не является словарем')
        elif 'name' not in data or not isinstance(data['name'], str):
            raise ValueError('Ошибка: Kлюч name не присутствует в словаре или его значение не является строкой')
        elif 'age' not in data or not isinstance(data['age'], int) or data['age'] <= 0:
            raise ValueError('Ошбика: Ключ age не присутствует в словаре или его значение не является положительным числом')
    except (TypeError, ValueError) as e:
        print(e)
    else: 
        print('Ошибок не обнаружено')
    finally:
        print('Проверка словаря завершена\n')
          

validate_user_input({"name": "Alice", "age": 30})
validate_user_input({"age": 30})
validate_user_input({"name": "Alice", "age": -30})
validate_user_input({"name": "Alice", "age": 'тридцать'})
validate_user_input("name: Alice, age: 30")


