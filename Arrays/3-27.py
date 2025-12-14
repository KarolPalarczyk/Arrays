# Zadanie 27: Drukowanie tablicy dwuwymiarowej 2x4

# Utworzenie dwuwymiarowej tablicy (listy list) 2 wiersze x 4 kolumny
# Wiersz 0: [1, 2, 3, 4]
# Wiersz 1: [5, 6, 7, 8]
two_d_array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Pobranie wymiarów tablicy (dla dynamicznego kodu)
num_rows = len(two_d_array)
num_cols = len(two_d_array[0]) if num_rows > 0 else 0

print(f"Tablica ma rozmiar: {num_rows} wierszy x {num_cols} kolumn.")
print("--- Zawartość tablicy ---")

# Iteracja przez wiersze
for row_index in range(num_rows):
    
    # Wyświetlenie nagłówka wiersza (opcjonalne)
    print(f"Wiersz {row_index}: ", end="")
    
    # Iteracja przez kolumny w bieżącym wierszu
    for col_index in range(num_cols):
        
        # Pobranie elementu
        element = two_d_array[row_index][col_index]
        
        # Wydrukowanie elementu. Używamy 'end=" "' aby pozostać w tym samym wierszu.
        print(f"{element:^5}", end="")  # Użycie formatowania :^5 zapewnia ładne wyrównanie

    # Po zakończeniu kolumn w wierszu, przechodzimy do nowej linii
    print()

print("--------------------------")