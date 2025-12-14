# Zadanie 32: Zamiana pierwszego i ostatniego wiersza w tablicy 3x5

def print_array(arr, title):
    """Pomocnicza funkcja do drukowania tablicy dwuwymiarowej."""
    print(f"\n--- {title} ---")
    for row in arr:
        # Użycie formatowania :>4 zapewnia ładne wyrównanie kolumn
        row_str = " ".join(f"{element:>4}" for element in row)
        print(row_str)

# 1. Utworzenie przykładowej dwuwymiarowej tablicy 3x5
# Liczba wierszy (ROWS) = 3
# Liczba kolumn (COLS) = 5
two_d_array = [
    [10, 11, 12, 13, 14],  # Wiersz 0 (pierwszy)
    [20, 21, 22, 23, 24],  # Wiersz 1
    [30, 31, 32, 33, 34]   # Wiersz 2 (ostatni)
]

# Pobranie indeksów
FIRST_ROW_INDEX = 0
# Indeks ostatniego wiersza to: długość tablicy - 1
LAST_ROW_INDEX = len(two_d_array) - 1

# 2. Wydrukowanie tablicy przed zmianą
print_array(two_d_array, "Tablica przed zamianą")

# 3. Zamiana pierwszego wiersza z ostatnim (w Pythonie jest to proste)
# Używamy destrukcyjnego przypisania
two_d_array[FIRST_ROW_INDEX], two_d_array[LAST_ROW_INDEX] = \
    two_d_array[LAST_ROW_INDEX], two_d_array[FIRST_ROW_INDEX]

# 4. Wydrukowanie tablicy po zmianie
print_array(two_d_array, "Tablica po zamianie")