# Zadanie 33: Zamiana pierwszej i ostatniej kolumny w tablicy 3x5

def print_array(arr, title):
    """Pomocnicza funkcja do drukowania tablicy dwuwymiarowej."""
    print(f"\n--- {title} ---")
    for row in arr:
        # Użycie formatowania :>4 zapewnia ładne wyrównanie kolumn
        row_str = " ".join(f"{element:>4}" for element in row)
        print(row_str)
    print("-" * 25)


# 1. Utworzenie przykładowej dwuwymiarowej tablicy 3x5
# Pierwsza kolumna to [10, 20, 30]
# Ostatnia kolumna to [14, 24, 34]
two_d_array = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]

# Pobranie indeksów kolumn
FIRST_COL_INDEX = 0
# Indeks ostatniej kolumny to: długość wiersza - 1
LAST_COL_INDEX = len(two_d_array[0]) - 1

# 2. Wydrukowanie tablicy przed zmianą
print_array(two_d_array, "Tablica przed zamianą kolumn")

# 3. Zamiana pierwszej kolumny z ostatnią
# Musimy wykonać zamianę dla każdego wiersza osobno.
for row_index in range(len(two_d_array)):
    # Dla każdego wiersza, zamień element z kolumny 0 z elementem z kolumny 4
    two_d_array[row_index][FIRST_COL_INDEX], two_d_array[row_index][LAST_COL_INDEX] = \
        two_d_array[row_index][LAST_COL_INDEX], two_d_array[row_index][FIRST_COL_INDEX]

# 4. Wydrukowanie tablicy po zmianie
print_array(two_d_array, "Tablica po zamianie kolumn")