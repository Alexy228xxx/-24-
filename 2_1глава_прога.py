#2.1
print("2.1)")
# a) y = 17x^2 - 6x + 13
x = float(input("Введите значение x: "))
y = 17 * x**2 - 6 * x + 13
print(f"Значение функции y: {y}")

# b) y = 3a^2 + 5a - 21
a = float(input("Введите значение a: "))
y = 3 * a**2 + 5 * a - 21
print(f"Значение функции y: {y}")
#2.2
print("2.2)")
a = float(input("Введите значение a: "))
result = (a**2 + 10) / ((a**2 + 1)**0.5)
print(f"Значение функции: {result}")
#2.3
print("2.3)")
import math

# a) √((2a + sin|3a|) / 3.56)
a = float(input("Введите значение a: "))
result = math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)
print(f"Значение функции: {result}")

# b) sin((3.2 + √(1 + x)) / |5x|)
x = float(input("Введите значение x: "))
result = math.sin((3.2 + math.sqrt(1 + x)) / abs(5 * x))
print(f"Значение функции: {result}")
#2.4
print("2.4)")
n = float(input("Введите длину стороны квадрата: "))
perimter = 4 * n
print(f"Периметр квадрата: {perimter}")
#2.5
print("2.5)")
radius = float(input("Введите радиус окружности: "))
diameter = 2 * radius
print(f"Диаметр окружности: {diameter}")
#2.6
print("2.6)")
R = 6350
h = float(input("Введите высоту над Землей: "))
distance = ((2 * R * h)**0.5)
print(f"Расстояние до линии горизонта: {distance:.2f} км")
#2.7
print("2.7)")
edge = float(input("Введите длину ребра куба: "))
volume = edge**3
surface_area = 6 * edge**2
print(f"Объем куба: {volume}, Площадь боковой поверхности: {surface_area}")
#2.8
print("2.8)")
import math

radius = float(input("Введите радиус окружности: "))
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print(f"Длина окружности: {circumference:.2f}, Площадь круга: {area:.2f}")
#2.9
print("2.9)")
# a) z = 2x^3 - 3.44xy + 2.3x^2 - 7.1y + 2
x, y = map(float, input("Введите значения x и y: ").split())
z = 2 * x**3 - 3.44 * x * y + 2.3 * x**2 - 7.1 * y + 2
print(f"Значение функции z: {z}")

# b) x = 3.14(a + b)^3 + 2.75b^2 - 12.7a - 4.1
a, b = map(float, input("Введите значения a и b: ").split())
x = 3.14 * (a + b)**3 + 2.75 * b**2 - 12.7 * a - 4.1
print(f"Значение функции x: {x}")
#2.10
print("2.10)")
num1, num2 = map(int, input("Введите два целых числа: ").split())
arithmetic_mean = (num1 + num2) / 2
geometric_mean = (num1 * num2)**0.5
print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")
