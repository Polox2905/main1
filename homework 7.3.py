class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with (open(file, 'r', encoding='utf-8') as f):
                content = f.read()
                content = content.lower()
                content = content.replace(',', '').replace('.', ''
                        ).replace('=', '').replace('!', ''
                        ).replace('?', '').replace(';', ''
                        ).replace(':', '').replace(' - ', '')
                words = content.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        found_positions = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            try:
                position = words.index(word) + 1  
                found_positions[name] = position
            except ValueError:
                pass
        return found_positions

    def count(self, word):
        counts = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            counts[name] = words.count(word)
        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего








