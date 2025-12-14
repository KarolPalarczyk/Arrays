# Zadanie 25: Rysowanie wykresu funkcji f(x) = x^2 - 3

import matplotlib.pyplot as plt

x = []
y = []

# # create x values
# Tworzenie wartości x od -100 do 100 (włącznie)
for n in range(-100, 101):
    x.append(n)

# # create y values
# Obliczanie wartości y dla każdego x, zgodnie ze wzorem f(x) = x^2 - 3
for val_x in x:
    # Wzór funkcji: y = x^2 - 3
    val_y = val_x**2 - 3
    y.append(val_y)

# # print chart

# Tworzenie wykresu
plt.figure(figsize=(10, 6)) # Ustawienie rozmiaru wykresu (opcjonalne)
plt.plot(x, y, color='red', label='$f(x) = x^2 - 3$') # Rysowanie linii

# Dodanie etykiet i tytułu
plt.title("Wykres funkcji kwadratowej $f(x) = x^2 - 3$")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

# Dodanie siatki i legendy
plt.grid(True)
plt.legend()

# Wyświetlenie wykresu
plt.show()