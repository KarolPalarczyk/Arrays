# Zadanie 31: Znajdowanie najmniejszej i największej wartości oraz ich lokalizacji

# Definicja tablicy dwuwymiarowej
two_d_array = [
    [-38, 19], 
    [5, 48], 
    [-7, 11], 
    [29, 16]
]

# Inicjalizacja zmiennych do śledzenia min/max i ich lokalizacji
# Pobieramy pierwszy element jako punkt odniesienia
initial_value = two_d_array[0][0]

min_value = initial_value
max_value = initial_value

# Lokalizacje są podawane jako (wiersz, kolumna)
min_location = (0, 0)
max_location = (0, 0)

# Iteracja przez tablicę za pomocą zagnieżdżonych pętli for z użyciem enumerate
for row_index, row in enumerate(two_d_array):
    # row_index to numer wiersza (0, 1, 2, 3)
    
    for col_index, value in enumerate(row):
        # col_index to numer kolumny (0, 1)
        
        # Sprawdzenie minimum
        if value < min_value:
            min_value = value
            min_location = (row_index, col_index)
            
        # Sprawdzenie maksimum
        if value > max_value:
            max_value = value
            max_location = (row_index, col_index)

# Wydruk wyników
print("--- Analiza tablicy ---")
for row in two_d_array:
    print(row)
    
print("\n--- Wyniki ---")

# Wynik dla minimum
print(f"Najmniejsza wartość (Min): {min_value}")
print(f"Lokalizacja (Wiersz, Kolumna): {min_location}")

# Wynik dla maksimum
print(f"Największa wartość (Max): {max_value}")
print(f"Lokalizacja (Wiersz, Kolumna): {max_location}")