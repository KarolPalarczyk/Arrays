# Zadanie 36: Funkcja konwertująca tablicę 2D na 1D i jej użycie

def convert_2d_to_1d(array_2d):
    """
    Konwertuje tablicę dwuwymiarową (listę list) na tablicę jednowymiarową (pojedynczą listę).
    
    :param array_2d: Lista list (tablica 2D)
    :return: Spłaszczona lista (tablica 1D)
    """
    # Użycie zagnieżdżonej listy składanej: 
    # Dla każdego elementu 'element' w każdym 'row' w 'array_2d', dodaj go do nowej listy.
    flat_array = [element for row in array_2d for element in row]
    return flat_array

def print_2d_array(arr, title):
    """Pomocnicza funkcja do drukowania tablicy 2D."""
    print(f"\n--- Macierz źródłowa ({title}) ---")
    for row in arr:
        row_str = " ".join(f"{element}" for element in row)
        print(row_str)

# --- Program główny ---

# Macierze źródłowe
matrix_i = [
    [1, 2], 
    [1, 5]
]
matrix_ii = [
    [5, 0, 3, 7, 5], 
    [9, 0, 9, 1, 2]
]
matrix_iii = [
    [2, 1], 
    [3, 5], 
    [7, 4], 
    [2, 6]
]

print("--- Spłaszczanie macierzy 2D na 1D ---")

# i. Macierz 2x2
print_2d_array(matrix_i, "i. 2x2")
flat_i = convert_2d_to_1d(matrix_i)
print(f"Wynik 1D: {flat_i}")

# ii. Macierz 2x5
print_2d_array(matrix_ii, "ii. 2x5")
flat_ii = convert_2d_to_1d(matrix_ii)
print(f"Wynik 1D: {flat_ii}")

# iii. Macierz 4x2
print_2d_array(matrix_iii, "iii. 4x2")
flat_iii = convert_2d_to_1d(matrix_iii)
print(f"Wynik 1D: {flat_iii}")