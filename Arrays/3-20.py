def separate_even_and_odd_by_new_list(arr):
    """
    Separuje liczby parzyste i nieparzyste w nowej liście,
    umieszczając wszystkie parzyste na początku, a następnie wszystkie nieparzyste.
    """
    even_numbers = []
    odd_numbers = []

    # Iteracja przez oryginalną tablicę i rozdzielanie liczb
    for number in arr:
        if number % 2 == 0:
            even_numbers.append(number)  # Parzyste
        else:
            odd_numbers.append(number)   # Nieparzyste

    # Łączenie list: najpierw parzyste, potem nieparzyste
    result_arr = even_numbers + odd_numbers
    return result_arr

# Przykładowe użycie na podstawie zadania:
arr = [7, 9, 2, 4, 5, 6]
print(f"Oryginalna tablica: {arr}")

result = separate_even_and_odd_by_new_list(arr)
print(f"Tablica po separacji: {result}")

# Inny przykład:
arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_2 = separate_even_and_odd_by_new_list(arr_2)
print(f"Oryginalna tablica: {arr_2}")
print(f"Tablica po separacji: {result_2}")