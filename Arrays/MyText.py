# Plik: MyText.py

# Zmienna zawierająca tekst
TEXT = "An apple a day keeps the doctor away"

def get_word_list(text):
    """
    Pomocnicza funkcja do podziału tekstu na listę słów.
    """
    # Użycie split() bez argumentów dzieli po białych znakach i ignoruje wielokrotne spacje.
    return text.split()

# i. Funkcja zwracająca liczbę słów w tekście
def count_words(text=TEXT):
    """
    Zwraca liczbę słów w podanym tekście.
    """
    words = get_word_list(text)
    return len(words)

# ii. Funkcja zwracająca uporządkowaną listę słów, od najdłuższego do najkrótszego
def sort_by_length_desc(text=TEXT):
    """
    Zwraca listę słów posortowaną malejąco według długości.
    """
    words = get_word_list(text)
    # key=len - sortuje po długości słowa
    # reverse=True - sortuje malejąco (od najdłuższego do najkrótszego)
    sorted_words = sorted(words, key=len, reverse=True)
    return sorted_words

# iii. Funkcja zwracająca alfabetycznie uporządkowaną listę słów
def sort_alphabetically(text=TEXT):
    """
    Zwraca listę słów posortowaną alfabetycznie.
    
    Uwaga: W Pythonie domyślne sortowanie (sort() lub sorted()) jest 
    czułe na wielkość liter, dlatego 'An' pojawi się przed 'a' i 'apple'.
    Jeśli chcemy sortować *bez* uwzględniania wielkości liter,
    należy użyć: sorted(words, key=str.lower)
    Poniższe rozwiązanie używa standardowego, czułego na wielkość liter sortowania.
    """
    words = get_word_list(text)
    # Domyślne sorted() sortuje alfabetycznie (rosnąco, czule na wielkość liter)
    sorted_words = sorted(words)
    return sorted_words