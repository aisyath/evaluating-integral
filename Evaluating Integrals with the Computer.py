import math

# Fungsi kecepatan parachutist
def y(t, g, m, c):
    return (g * m / c) * (1 - math.exp(-2 * (c / m) * t))

# Fungsi aturan trapesium untuk satu segmen
def Trap(h, f0, f1):
    return h * (f0 + f1) / 2

# Fungsi aturan trapesium untuk multiple segmen
def Trapm(h, n, g, m, c):
    sum_result = y(0, g, m, c) + y(0.8, g, m, c)  # First and last terms in the sum

    for i in range(1, n):
        t = i * h
        sum_result += 2 * y(t, g, m, c)

    return 0.5 * h * sum_result

# Nilai yang diberikan
g_value = 9.8  # Gravitasi bumi (m/s^2)
m_value = 68.1  # Massa pesawat terjun (kg)
c_value = 12.5  # Koefisien hambatan udara (kg/s)
t_value = 0.8  # Waktu maksimum

# Nilai eksak
exact_value = 289.43515

# Loop untuk menghitung integral dengan berbagai jumlah segmen
for n in [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]:
    h = t_value / n
    result = Trapm(h, n, g_value, m_value, c_value)
    error_percentage = abs((exact_value - result) / exact_value) * 100

    print(f"Segments: {n}, Segment Size: {h:.4f}, Estimated d: {result:.4f}, Et (%): {error_percentage:.4f}")
