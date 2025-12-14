# Zadanie 34: Tworzenie i drukowanie macierzy jednostkowej (identity matrix)

# A. Funkcja tworząca macierz jednostkową
def identity_matrix(n):
    """
    Tworzy i zwraca macierz jednostkową (n x n).
    Wymaga, aby elementy na głównej przekątnej (i=j) były równe 1, 
    a pozostałe 0.
    
    :param n: Rozmiar macierzy (n x n)
    :return: Lista list reprezentująca macierz jednostkową
    """
    matrix = []
    
    for i in range(n):
        row = []
        for j in range(n):
            # Jeśli indeks wiersza (i) jest równy indeksowi kolumny (j),
            # to jesteśmy na głównej przekątnej - ustawiamy 1
            if i == j:
                row.append(1)
            # W przeciwnym razie ustawiamy 0
            else:
                row.append(0)
        matrix.append(row)
        
    return matrix

# B. Funkcja drukująca tablicę 2D
def print_2d_array(arr):
    """
    Drukuje zawartość dwuwymiarowej tablicy (listy list) w formacie wiersz-kolumna.
    """
    for row in arr:
        # Używamy f-string do wyświetlenia każdego elementu z ładnym odstępem.
        row_str = " ".join(f"{element}" for element in row)
        print(row_str)
    print("-" * 15) # Separator po wydrukowaniu macierzy

# C. Program główny drukujący trzy macierze
print("--- Macierze jednostkowe ---")

# 1. Macierz 3x3
n3 = 3
matrix3 = identity_matrix(n3)
print(f"Macierz jednostkowa {n3}x{n3}:")
print_2d_array(matrix3)

# 2. Macierz 5x5
n5 = 5
matrix5 = identity_matrix(n5)
print(f"Macierz jednostkowa {n5}x{n5}:")
print_2d_array(matrix5)

# 3. Macierz 8x8
n8 = 8
matrix8 = identity_matrix(n8)
print(f"Macierz jednostkowa {n8}x{n8}:")
print_2d_array(matrix8)