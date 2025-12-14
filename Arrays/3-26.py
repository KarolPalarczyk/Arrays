# Zadanie 26: Rysowanie wykresu funkcji y = sin(x) w zakresie 0-360 stopni

import matplotlib.pyplot as plt
import numpy as np
import math

# 1. Tworzenie wartości x (kąty w stopniach)
# Używamy numpy.arange, aby uzyskać dużą liczbę punktów w zakresie 0 do 360,
# co zapewni gładką krzywą. Krok 1 stopień jest wystarczający.
x_degrees = np.arange(0, 361, 1)

# 2. Konwersja stopni na radiany
# Funkcje trygonometryczne w NumPy i Pythonie przyjmują radiany.
# Używamy funkcji numpy.radians() do masowej konwersji.
x_radians = np.radians(x_degrees)

# 3. Obliczanie wartości y
# Obliczamy sinus dla wszystkich radianów jednocześnie.
y = np.sin(x_radians)

# 4. Tworzenie wykresu
plt.figure(figsize=(10, 5)) # Ustawienie rozmiaru wykresu

# Rysowanie linii
plt.plot(x_degrees, y, color='darkgreen', label='$y = \sin(x)$')

# Ustawienie etykiet i tytułu
plt.title("Wykres funkcji $y = \sin(x)$ w zakresie $0^{\\circ} - 360^{\\circ}$")
plt.xlabel("Kąt (stopnie)")
plt.ylabel("Wartość $\sin(x)$")

# Ustawienie osi X tak, by były widoczne główne punkty (0, 90, 180, 270, 360)
plt.xticks(np.arange(0, 361, 90))

# Ustawienie siatki i legendy
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 5. Wyświetlenie wykresu
plt.show()