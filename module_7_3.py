import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')
                    words = content.split() 
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_positions = {}

        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
            else:
                word_positions[file_name] = None
        return word_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_count = {}

        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)
        return word_count


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 16 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего

"""
Содержимое файла test_file.txt:

Мне лень переписывать
Текст из примера задания для test_file,
Поэтому i believe i can fly:
text, TExt, teeext, TEXT, и снова, teXt
"""
