import re
from collections import Counter


def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            num_characters = len(text)
            words = re.findall(r'\b\w+\b', text)
            num_words = len(words)
            sentences = re.split(r'[.!?]+', text)
            num_sentences = len([s for s in sentences if s.strip()])
            word_counts = Counter(words)
            most_common_words = word_counts.most_common(10)

            print(f"Общее количество символов: {num_characters}")
            print(f"Общее количество слов: {num_words}")
            print(f"Общее количество предложений: {num_sentences}")
            print("\n10 самых частых слов:")
            for word, count in most_common_words:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запуск анализа
file_path = input("Введите путь к текстовому файлу: ")
analyze_text(file_path)
