# Zadanie 28: Obliczanie sumy wartości w ostatniej kolumnie tablicy dwuwymiarowej

# Definicja tablicy dwuwymiarowej (4 wiersze x 5 kolumn)
two_d_array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Wymiary tablicy
num_rows = len(two_d_array)
# Indeks ostatniej kolumny. Jeśli kolumna ma 5 elementów, indeksy to 0, 1, 2, 3, 4.
# Indeks ostatniej kolumny to: długość_wiersza - 1
last_col_index = len(two_d_array[0]) - 1

total_sum = 0
last_column_elements = []

# Iteracja przez każdy wiersz tablicy
for row in two_d_array:
    # Pobranie elementu z ostatniej kolumny bieżącego wiersza
    # Używamy indeksu [last_col_index]
    element = row[last_col_index]
    
    # Dodanie elementu do sumy
    total_sum += element
    
    # Zapisanie elementu do listy (dla celów wizualizacji wyniku)
    last_column_elements.append(element)

# Wyświetlenie wyników
print("--- Tablica źródłowa (ostatnia kolumna jest wytłuszczona) ---")
for row in two_d_array:
    # Wytłuszczenie ostatniego elementu podczas drukowania
    row_str = " ".join(map(str, row[:-1])) + f" **{row[-1]}**"
    print(row_str)

print("\n--- Wynik ---")
print(f"Elementy w ostatniej kolumnie: {last_column_elements}")
print(f"Suma wartości w ostatniej kolumnie: {total_sum}")