def is_subset_using_sets(arr1, arr2):
    """
    Sprawdza, czy arr1 jest podzbiorem arr2, używając zbiorów.

    arr1 (podzbiór) musi zawierać się w arr2 (zbiór główny).
    """
    # 1. Konwertujemy obie tablice na zbiory (sets).
    # Zbiory pozwalają na bardzo szybkie sprawdzenie przynależności (O(1)).
    set1 = set(arr1)
    set2 = set(arr2)

    # 2. Używamy operatora '<=' (less than or equal to) dla zbiorów,
    # który w Pythonie oznacza "czy jest podzbiorem".
    # set1 <= set2 oznacza, że wszystkie elementy set1 są również w set2.
    return set1 <= set2

# --- Przykłady użycia ---

# Przykład 1: arr1 jest podzbiorem arr2 (True)
arr_main_1 = [10, 20, 30, 40, 50]
arr_sub_1 = [20, 50, 10]
result_1 = is_subset_using_sets(arr_sub_1, arr_main_1)
print(f"Czy {arr_sub_1} jest podzbiorem {arr_main_1}? -> {result_1}")

# Przykład 2: arr1 nie jest podzbiorem arr2 (False)
arr_main_2 = [1, 2, 3]
arr_sub_2 = [1, 2, 3, 4]  # 4 brakuje w arr_main_2
result_2 = is_subset_using_sets(arr_sub_2, arr_main_2)
print(f"Czy {arr_sub_2} jest podzbiorem {arr_main_2}? -> {result_2}")

# Przykład 3: Podzbiór z duplikatami (nadal działa, ponieważ zbiór eliminuje duplikaty)
arr_main_3 = [5, 6, 7]
arr_sub_3 = [5, 5, 7, 7]
result_3 = is_subset_using_sets(arr_sub_3, arr_main_3)
print(f"Czy {arr_sub_3} jest podzbiorem {arr_main_3}? -> {result_3}")