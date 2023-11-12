import math

# Single-segment Trapezoidal Rule
def Trap(h, f0, f1):
    return h * (f0 + f1) / 2

# Multiple-segment Trapezoidal Rule
def Trapm(h, n, f):
    sum_result = f(0)

    for i in range(1, n - 1):
        t = i * h
        sum_result += 2 * f(t)

    sum_result += f(n * h)
    
    return h * sum_result / 2

# Fungsi y(t) untuk velocity
def y(t):
    # Definisi fungsi sesuai persamaan E21.3.1
    g = 9.8  # Gravitasi bumi (m/s^2)
    m = 68.1  # Massa pesawat terjun (kg)
    c = 12.5  # Koefisien hambatan udara (kg/s)
    return (g * m / c) * (1 - math.exp(-2 * (c / m) * t))

# Contoh penggunaan metode Trapezoidal
h_value = 0.4
n_value = 2
result_trapezoidal = Trapm(h_value, n_value, y)
print(f"Segments: {n_value}, Distance: {result_trapezoidal}")
