# Import library atau module yang diperlukan (jika ada)
import math

# Definisikan semua fungsi yang diperlukan, termasuk Trapezoidal, Simpson's, dan Uneven

# Trapezoidal rule for unequally spaced data
def Trapun(x, y, n):
    sum_result = 0

    for i in range(1, n):
        sum_result += (x[i] - x[i - 1]) * (y[i - 1] + y[i]) / 2

    return sum_result

# Simpson's 1/3 Rule
def Simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

# Simpson's 3/8 Rule
def Simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

# Uneven spaced data integration using combination of Simpson's and Trapezoidal rules
def Uneven(n, x, f):
    h = x[1] - x[0]
    sum_result = 0

    if n == 1:
        return Trapun(x, f, n)
    else:
        m = n
        odd = n // 2 - int(n % 2 == 0)

        if odd == 0 and n > 1:
            sum_result = Simp38(h, f[n - 3], f[n - 2], f[n - 1], f[n - 1])
            m = n - 3

        if m % 2 == 1 and m > 2:  # Perbaikan indeks untuk m yang ganjil
            sum_result += Simp13(h, f[m - 3], f[m - 2], f[m - 1])

    return sum_result

# Contoh penggunaan metode Trapezoidal untuk data tidak merata
x_values = [0, 0.2, 0.4, 0.6, 0.8]
y_values = [1.0688, 1.3695, 1.4848, 1.5399, 1.5703]
n_values = len(x_values)

result_trapezoidal_uneven = Trapun(x_values, y_values, n_values)
print(f"Segments: {n_values}, Distance: {result_trapezoidal_uneven}")

# Contoh penggunaan metode kombinasi untuk data tidak merata
result_combination_uneven = Uneven(n_values, x_values, y_values)
print(f"Segments: {n_values}, Distance: {result_combination_uneven}")
