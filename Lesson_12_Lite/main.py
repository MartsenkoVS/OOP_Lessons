import os
import logging
import chardet
import json
import time
import shutil
import datetime
import pprint
from jsonschema import validate, ValidationError
 
# Создаем папку для записи логов
os.makedirs('logs', exist_ok=True)

# Создаем логер
logging.basicConfig(
    filename='logs/app.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Задание 1
project_root = os.getcwd()

# Список со структурой директорий проекта
structure_list = [
    {"parent_dir": project_root, "subdirs": ["data", "logs", "backups", "output"]},
    {"parent_dir": "data", "subdirs": ["raw", "processed"]}
]

# В цикле создаем директории
for structure in structure_list:
    os.chdir(structure["parent_dir"])
    for subdir in structure["subdirs"]:
        if not os.path.exists(subdir):
            os.mkdir(subdir)
            logging.info(f'В директории {structure["parent_dir"]}/ создана директория {subdir}/')
        
# Возвращаемся в корневую директорию проекта         
os.chdir(project_root)

raw_dir = 'data/raw'

# Список для создания текстовых файлов
files_list=[
    {"name": "file_1.txt", "encoding": "UTF-8", "text": "Текстовый файл"},
    {"name": "file_2.txt", "encoding": "ISO-8859-1", "text": "text file"},
]

# В цикле создаем файлы и записываем информацию в лог
for file in files_list:
    file_path = os.path.join(raw_dir, file["name"])
    
    with open(file_path, 'w', encoding=file["encoding"]) as f:
        f.write(file["text"])
    logging.info(f'В директории {raw_dir}/ создан файл {file["name"]}')
 
       
# Задание 2
processed_dir = 'data/processed'
output_dir = 'output'
data_json = {}

#
for i, file in enumerate(os.listdir(raw_dir)):
    file_path = os.path.join(raw_dir, file)
    
    # Открываем файл, определяем кодировку, читаем текст, меняем формат букв в тексте
    with open(file_path, 'rb') as f:
       raw_data = f.read()
       result = chardet.detect(raw_data)
       encoding = result['encoding']
       print(f'Прочитан файл {file} с кодировкой {encoding}')
       text = raw_data.decode(encoding)
       processed_text = text.swapcase()
       
    # меняем название файла
    processed_file_name = f'{file[:-4]}_processed.txt'
    file_path = os.path.join(processed_dir, processed_file_name)
    
    # записываем измененный текст в новый файл
    with open(file_path, 'w') as f:
        f.write(processed_text)
    logging.info(f'В директории {processed_dir}/ создан файл {processed_file_name}')
        
    # создаем словарь для записи в json
    data_json[f"file_{i+1}"] = {
        "name": processed_file_name,
        "text": text,
        "processed_text": processed_text,
        "size": os.path.getsize(file_path),
        "last_change_date": time.ctime(os.path.getmtime(file_path))
    }
# записываем в json файл
json_file = 'processed_data.json'
json_path = os.path.join(output_dir, json_file)
with open(json_path, 'w') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=4)
logging.info(f'В директории {output_dir}/ создан файл {json_file}')

       
# Задание 3
backup_dir = 'backups'
dir_for_archive = 'data'
archive = f'backup_{datetime.date.today()}.zip'
archive_path = os.path.join(backup_dir, archive)

# Архивируем директорию
shutil.make_archive(archive_path[:-4], 'zip', dir_for_archive)
logging.info(f'Директория {dir_for_archive}/ заархивирована, архив добавлен в директорию {backup_dir}/')

# Восстанавливаем директорию из архива
shutil.unpack_archive(archive_path, archive[:-4])
logging.info(f'Из директории {backup_dir} разархивирован {archive} в директорию {archive[:-4]}')


# Задание 4
class FileInfo():
    """Kласс для хранения информации о файле"""
    def __init__(self, file_path: str):
        self.name = os.path.basename(file_path)
        self.abs_path = os.path.abspath(file_path)
        self.size = os.path.getsize(file_path)
        self.create_date = time.ctime(os.path.getctime(file_path))
        self.last_change_date = time.ctime(os.path.getmtime(file_path))

    
def file_info_to_dict(file_info: FileInfo) -> dict:
    """
    Функция на вход получает объект класса FileInfo, 
    преобразовывает информацию о файле в формат для json
    """
    file_info_dict = {
        "name": file_info.name,
        "abs_path": file_info.abs_path, 
        "size": file_info.size,
        "create_date": file_info.create_date,
        "last_change_date": file_info.last_change_date
    }
    return file_info_dict

json_file = 'processed_data_2.json'
json_path = os.path.join(output_dir, json_file)
data_json = {"files": []}

# В цикле по каждому файлу создаем объект класса FileInfo и передаем его в функцию file_info_to_dict,
# полученный словарь добавляем в список в json словарь по ключу "files"
for file in os.listdir(processed_dir):
    file_path = os.path.join(processed_dir, file)
    file_info = FileInfo(file_path)
    data_json["files"].append(file_info_to_dict(file_info))
    
# записываем в json файл    
with open(json_path, 'w') as f:
    json.dump(data_json, f, indent=4)
logging.info(f'В директории {output_dir}/ создан файл {json_file}')

# читаем json файл, для более аккуратного вывода словаря используем pprint 
with open(json_path, 'r') as f:
    json_string = json.load(f)
print('Десериализованные данные:')
pprint.pprint(json_string)

# json схема
schema = {
    "type": "object",
    "properties": {
        "files": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "abs_path": {
                        "type": "string"
                    },
                    "size": {
                        "type": "integer"
                    },
                    "create_date": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "last_change_date": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "required": ["name", "abs_path", "size", "create_date", "last_change_date"]
            }
        }
    },
    "required": ["files"]
}

# Валидация json (правильный вариант)
try:
    validate(instance=data_json, schema=schema)
    print('Файл валиден')
except ValidationError as e:
    print(f'Файл не прошел валидацию, ошибка:{e}')
    
# Валидация json (вариант c ошибками)
# Скопируем data_json в новую переменную и специально удалим обязательное поле "name"
no_valid_data_json = data_json
no_valid_data_json["files"][0].pop("name")

try:
    validate(instance=data_json, schema=schema)
    print('Файл валиден')
except ValidationError as e:
    print(f'Файл не прошел валидацию, ошибка:{e}')
    logging.error(f'Файл не прошел валидацию, ошибка:{e}')


# Задание 5
# Создаем структуру для формирования json файла с отчетом по всем заданиям
report_data = [
    {
        "task_number": 1,
        "dificultades": "Нужно было придумать, как сформировать структуру для создания директорий, чтобы пройтись по ней циклом",
        "soluciones": "Создал список со словарями, где ключ это родительская директория, а значение - список с поддиректориями",
        "time_to_complite": {"time": 1, "format": "hour"},
        "improvements": "Обернуть код в функцию с атрибутом structure_list (структура директорий в проекте)",
    },
    {
        "task_number": 2,
        "dificultades": "При сохранении текста с кодировкой ISO-8859-1 в json файле отображалась кодировка, а не сам текст",
        "soluciones": "В методе json.dump() добавил параметр ensure_ascii=False",
        "time_to_complite": {"time": 1, "format": "hour"},
        "improvements": "Обернуть код в функцию с атрибутами files_list (инфо о файлах) и dir (директория, куда записать файлы)",
    },
    {
        "task_number": 3,
        "dificultades": None,
        "soluciones": None,
        "time_to_complite": {"time": 15, "format": "minutes"},
        "improvements": "Обернуть код в функцию с атрибутами archive_path (куда сохранять архив) и dir (директория, которую архивируем)",
    },
    {
        "task_number": 4,
        "dificultades": "Формат моего json файла отличался файла в лекции, не знал, как в json схеме указать элементы массива",
        "soluciones": "Спросил у ChatGPT, добавил поле items в схему",
        "time_to_complite": {"time": 1, "format": "hour"},
        "improvements": "Обернуть код валидации json в функцию с атрибутами json_file и json_schema",
    }
]

# Записываем отчет в json файл
json_path = 'output/report.json'
with open(json_path, 'w') as f:
    json.dump(report_data, f, ensure_ascii=False, indent=4)
logging.info(f'В директории {output_dir}/ создан файл {json_file}')
    

           
        

