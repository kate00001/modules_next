def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for i, string in enumerate(strings, start=1):
            start_byte = f.tell()
            f.write(string + '\n')
            strings_positions[(i, start_byte)] = string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for y in result.items():
    print(y)

"""
Содержимое файла test.txt:

Text for tell.
Используйте кодировку utf-8.
Because there are 2 languages!
Спасибо!
"""