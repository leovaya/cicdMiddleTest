from text_analyzer import TextAnalyzer 


def main():
    file_path = "text_file.txt"  

    try:
        analyzer = TextAnalyzer(file_path) 
        words, sentences = analyzer.analyze()  

        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено! Переконайтеся, що 'text_file.txt' існує.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()