## 21. Program sprawdzający, czy arr1 jest podzbiorem arr2

def is_subset(arr1, arr2):
    """
    Sprawdza, czy wszystkie elementy z arr1 występują w arr2.
    Nie uwzględnia częstotliwości (duplikatów).
    """
    # Konwersja drugiej (większej) tablicy na zbiór dla szybkiego sprawdzania obecności (O(1))
    set2 = set(arr2)

    # Iteracja przez elementy mniejszej tablicy
    for element in arr1:
        # Jeśli element z arr1 nie jest znaleziony w set2, arr1 nie jest podzbiorem
        if element not in set2:
            return False

    # Jeśli wszystkie elementy z arr1 zostały znalezione, jest to podzbiór
    return True

# --- Przykłady użycia ---

# Przykład A: Jest podzbiorem (True)
array_A = [10, 30, 10]
array_B = [50, 10, 40, 30, 20]
print(f"Czy {array_A} jest podzbiorem {array_B}? -> {is_subset(array_A, array_B)}")

# Przykład B: Nie jest podzbiorem (False - brakuje 7)
array_C = [7, 8, 9]
array_D = [9, 8, 1, 2]
print(f"Czy {array_C} jest podzbiorem {array_D}? -> {is_subset(array_C, array_D)}")

# Przykład C: Porównanie pustej tablicy (True - pusta jest zawsze podzbiorem)
array_E = []
array_F = [1, 2, 3]
print(f"Czy {array_E} jest podzbiorem {array_F}? -> {is_subset(array_E, array_F)}")