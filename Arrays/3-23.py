# Plik: main_program.py

# Importowanie modułu MyText (zakładając, że plik MyText.py znajduje się w tym samym katalogu)
import MyText

# Definicja tekstu do analizy (pobranego ze stałej w module)
text_to_analyze = MyText.TEXT

print(f"Text: {text_to_analyze}")
print("-" * 30)

# i. Liczba słów
num_words = MyText.count_words()
print(f"Number of words: {num_words}")

# ii. Słowa posortowane od najdłuższego
words_by_length = MyText.sort_by_length_desc()
print(f"Words from the longest: {', '.join(words_by_length)}")

# iii. Słowa posortowane alfabetycznie
words_alphabetical = MyText.sort_alphabetically()
print(f"Words ordered alphabetically: {', '.join(words_alphabetical)}")