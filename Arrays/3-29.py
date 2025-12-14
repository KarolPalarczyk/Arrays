# Zadanie 29: Tworzenie i drukowanie dwuwymiarowej tablicy wypełnionej zerami

def create_2d_arr(rows, cols):
    """
    Tworzy i zwraca dwuwymiarową tablicę (listę list) o podanych wymiarach 
    wypełnioną wartościami 0.
    
    :param rows: Liczba wierszy (x)
    :param cols: Liczba kolumn (y)
    :return: Lista list
    """
    # Użycie zagnieżdżonej listy składanej: 
    # [ [0, 0, ..., 0] dla każdej z 'rows' ]
    zero_array = [[0 for _ in range(cols)] for _ in range(rows)]
    return zero_array

# 1. Tworzenie dwuwymiarowej tablicy o wymiarach 3 na 5
ROWS = 4
COLS = 5
new_array = create_2d_arr(ROWS, COLS)

print(f"--- Tworzenie tablicy {ROWS}x{COLS} ---")
print(f"Wymiary: {ROWS} wierszy (x) na {COLS} kolumn (y)")

# 2. Drukowanie stworzonej tablicy
print("\n--- Zawartość tablicy ---")
for row_index, row in enumerate(new_array):
    # Używamy f-string do wyświetlenia każdego wiersza w czytelny sposób
    print(f"Wiersz {row_index}: {row}")