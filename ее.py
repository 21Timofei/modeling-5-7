import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Параметры для моделирования
v0 = 50            # начальная скорость (м/с)
alpha = np.radians(45)  # угол броска (в радианах)
y0 = 0             # начальная высота (м)
k = 0.1            # коэффициент сопротивления воздуха
m = 1              # масса тела (кг)
g = 9.81           # ускорение свободного падения (м/с^2)

# Начальные условия
v_x0 = v0 * np.cos(alpha)
v_y0 = v0 * np.sin(alpha)
initial_conditions = [0, y0, v_x0, v_y0]  # x0, y0, vx0, vy0

# Уравнения движения с учетом сопротивления воздуха
def equations(t, state):
    x, y, vx, vy = state
    v = np.sqrt(vx**2 + vy**2)  # Модуль скорости
    ax = -k/m * vx  # Ускорение по x
    ay = -g - k/m * vy  # Ускорение по y
    return [vx, vy, ax, ay]

# Решение ОДУ
t_span = (0, 10)  # временной интервал
t_eval = np.linspace(*t_span, 500)  # временные точки для записи решения
solution = solve_ivp(equations, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Извлечение данных
x, y, vx, vy = solution.y
t = solution.t
v = np.sqrt(vx**2 + vy**2)  # Модуль скорости

# Построение графиков
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Траектория движения
axes[0].plot(x, y, label="Траектория движения")
axes[0].set_xlabel("x (м)")
axes[0].set_ylabel("y (м)")
axes[0].set_title("Траектория движения тела")
axes[0].grid()
axes[0].legend()

# Зависимость скорости от времени
axes[1].plot(t, v, label="Скорость")
axes[1].set_xlabel("Время (с)")
axes[1].set_ylabel("Скорость (м/с)")
axes[1].set_title("Зависимость скорости от времени")
axes[1].grid()
axes[1].legend()

# Координаты от времени
axes[2].plot(t, x, label="x(t)")
axes[2].plot(t, y, label="y(t)")
axes[2].set_xlabel("Время (с)")
axes[2].set_ylabel("Координаты (м)")
axes[2].set_title("Зависимость координат от времени")
axes[2].grid()
axes[2].legend()

plt.tight_layout()
plt.show()