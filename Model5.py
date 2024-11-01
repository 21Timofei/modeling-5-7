# Re-importing libraries after environment reset
import numpy as np
import matplotlib.pyplot as plt

# Параметры для моделирования потенциального поля
k = 1  # коэффициент жесткости
n = 100  # количество точек вдоль осей x и y

# Создание сетки для координат x и y
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)

# Расчет потенциальной энергии U(x, y) для поля упругости
U = 0.5 * k * (X**2 + Y**2)

# Построение карты уровня для визуализации потенциального поля
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, U, levels=50, cmap="viridis")
plt.colorbar(contour, label="Потенциальная энергия U(x, y)")
plt.title("Двумерное распределение потенциальной энергии U(x, y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()