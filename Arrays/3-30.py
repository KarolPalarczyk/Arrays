# Zadanie 30: Tworzenie i drukowanie tablicy mnożenia 5x5

# 1. Definicja początkowej tablicy (5x5 wypełnionej zerami)
# Zadanie sugeruje taką inicjalizację:
multiplication_array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Wymiary tablicy (dla tablicy 5x5, indeksy będą od 0 do 4)
ROWS = 5
COLS = 5

# 2. Modyfikacja tablicy za pomocą pętli (tworzenie tabliczki mnożenia)
for i in range(ROWS):
    # i to indeks wiersza (0, 1, 2, 3, 4)
    
    for j in range(COLS):
        # j to indeks kolumny (0, 1, 2, 3, 4)
        
        # Wartości w tablicy mnożenia zaczynają się od 1x1.
        # Dlatego dodajemy 1 do indeksów i oraz j.
        # Wartość w komórce [i][j] = (i+1) * (j+1)
        multiplication_array[i][j] = (i + 1) * (j + 1)

# 3. Drukowanie tablicy w czytelnym formacie (jak w przykładzie)
print("--- Tablica mnożenia 5x5 ---")
for row in multiplication_array:
    # Używamy f-string i mapowania, aby ładnie wyrównać liczby. 
    # :>3 zapewnia wyrównanie do prawej i minimum 3 znaki szerokości.
    row_str = " ".join(f"{element:>3}" for element in row)
    print(row_str)