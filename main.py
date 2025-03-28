from text_analyzer import TextAnalyzer  # Імпортуємо клас
def main():
    file_path = "test_file.txt"  # Вкажи свій файл

    try:
        analyzer = TextAnalyzer(file_path)  # Створюємо об'єкт
        words, sentences = analyzer.analyze()  # Викликаємо метод аналізу

        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено! Переконайтеся, що 'test_file.txt' існує.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()