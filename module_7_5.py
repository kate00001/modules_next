import os
import time


def explore_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


directory = "."
explore_directory(directory)

"""
У меня тут много файлов нашлось:

Обнаружен файл: module_7_1.py, Путь: .\module_7_1.py, Размер: 1682 байт, Время изменения: 04.10.2024 01:17, Родительская директория: .
Обнаружен файл: module_7_2.py, Путь: .\module_7_2.py, Размер: 753 байт, Время изменения: 06.10.2024 22:46, Родительская директория: .
Обнаружен файл: module_7_3.py, Путь: .\module_7_3.py, Размер: 1962 байт, Время изменения: 07.10.2024 16:05, Родительская директория: .
Обнаружен файл: module_7_4.py, Путь: .\module_7_4.py, Размер: 1722 байт, Время изменения: 07.10.2024 16:27, Родительская директория: .
Обнаружен файл: module_7_5.py, Путь: .\module_7_5.py, Размер: 726 байт, Время изменения: 07.10.2024 16:39, Родительская директория: .
Обнаружен файл: products.txt, Путь: .\products.txt, Размер: 97 байт, Время изменения: 04.10.2024 11:49, Родительская директория: .
Обнаружен файл: test.txt, Путь: .\test.txt, Размер: 115 байт, Время изменения: 06.10.2024 22:44, Родительская директория: .
Обнаружен файл: test_file.txt, Путь: .\test_file.txt, Размер: 189 байт, Время изменения: 07.10.2024 16:05, Родительская директория: .
"""
