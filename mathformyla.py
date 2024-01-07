import math

a = float(input("Введите угол a в градусах: "))
a_rad = math.radians(a) # переводим угол в радианы

# Расчет по первой формуле
z1 = 1 - 2 * math.sin(a_rad)**2 / (1 + math.sin(2 * a_rad))
print("z1 =", z1)

# Расчет по второй формуле
z2 = 1 - math.tan(a_rad) / (1 + math.tan(a_rad))
print("z2 =", z2)
