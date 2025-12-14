# Zadanie 35: Funkcja zwracająca macierz transponowaną i jej drukowanie

def transpose_matrix(m):
    """
    Zwraca macierz transponowaną dla podanej macierzy m.
    
    Wymiary m: R wierszy x C kolumn
    Wymiary transponowanej macierzy: C wierszy x R kolumn
    """
    if not m:
        return []
    
    # Liczba wierszy w oryginalnej macierzy (R)
    num_rows = len(m)
    # Liczba kolumn w oryginalnej macierzy (C)
    num_cols = len(m[0])
    
    # Tworzenie nowej macierzy transponowanej o wymiarach num_cols x num_rows
    # Użycie zagnieżdżonej listy składanej jest bardzo efektywne
    
    transposed = []
    # Iterujemy po nowej liczbie wierszy (oryginalne kolumny)
    for j in range(num_cols):
        # Tworzymy nowy wiersz, który będzie kolumną j z oryginalnej macierzy
        new_row = [m[i][j] for i in range(num_rows)]
        transposed.append(new_row)
        
    return transposed

def print_2d_array(arr, title="Macierz"):
    """
    Drukuje zawartość dwuwymiarowej tablicy (listy list).
    """
    print(f"\n--- {title} ---")
    for row in arr:
        # Używamy f-string do wyświetlenia każdego elementu z ładnym odstępem.
        row_str = " ".join(f"{element:>3}" for element in row)
        print(row_str)
    print("-" * 25) 


# --- Program główny ---

# Macierze źródłowe
matrix_i = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
matrix_ii = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 0]
]
matrix_iii = [
    [5, 6, 7, 8]
]

# i. Macierz 3x3
print_2d_array(matrix_i, "Macierz źródłowa (i): 3x3")
transposed_i = transpose_matrix(matrix_i)
print_2d_array(transposed_i, "Macierz transponowana (i): 3x3")

# ii. Macierz 2x5
print_2d_array(matrix_ii, "Macierz źródłowa (ii): 2x5")
transposed_ii = transpose_matrix(matrix_ii)
print_2d_array(transposed_ii, "Macierz transponowana (ii): 5x2")

# iii. Macierz 1x4
print_2d_array(matrix_iii, "Macierz źródłowa (iii): 1x4")
transposed_iii = transpose_matrix(matrix_iii)
print_2d_array(transposed_iii, "Macierz transponowana (iii): 4x1")