# Zadanie 24: Wizualizacja danych za pomocą Matplotlib

import matplotlib.pyplot as plt

# 1. Definicja punktów X i Y
# Punkty X (pozioma oś): Zaczyna się w x=1, kończy w x=8
x_points = [1, 8]

# Punkty Y (pionowa oś): Zaczyna się w y=3, kończy w y=10
y_points = [3, 10]

# 2. Tworzenie wykresu
# plt.plot(x, y) łączy punkty z listy x z odpowiadającymi im punktami z listy y
plt.plot(x_points, y_points, marker='o', linestyle='-', color='blue')

# Dodanie tytułu i etykiet dla lepszej czytelności (opcjonalnie, ale zalecane)
plt.title("Wykres liniowy Matplotlib")
plt.xlabel("Oś X (Pozycja x)")
plt.ylabel("Oś Y (Pozycja y)")

# Opcjonalnie: Ustawienie siatki, aby punkty były łatwiejsze do zlokalizowania
plt.grid(True)

# Opcjonalnie: Zaznaczenie punktów (1, 3) i (8, 10) na wykresie
plt.text(1, 3, '(1, 3)', fontsize=10, ha='right')
plt.text(8, 10, '(8, 10)', fontsize=10, ha='left')

# 3. Wyświetlenie wykresu
plt.show()