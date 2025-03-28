class TextAnalyzer:
    def __init__(self, file_path):
        
        self.text = self.__read_file(file_path)
    
    def __read_file(self, file_path):
    
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Помилка: Файл '{file_path}' не знайдено.")
            return ""
    
    def __count_words(self):
    
        if not self.text:
            return 0
        
        words_delimiters = {' ', ',', ':', ';'}
        words_count = 0
        word = False  
        
        for char in self.text:
            if char in words_delimiters:
                if word:
                    words_count += 1
                    word = False
            else:
                word = True
        
        if word: 
            words_count += 1
        
        return words_count
    def __count_sentences(self):
        
        if not self.text:
            return 0
        
        sentences_endings = {'.', '!', '?'}
        sentences_count = 0
        i = 0
        
        while i < len(self.text):
            if self.text[i] in sentences_endings:
                if self.text[i:i+3] == '...':  
                    i += 2  
                sentences_count += 1
            i += 1
        
        if self.text[-1] not in sentences_endings and self.__count_words() > 0:
            sentences_count += 1
        
        return sentences_count

    def analyze(self):
        
        return self.__count_words(), self.__count_sentences()

