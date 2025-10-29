#2.11
print("2.11)")
mass = float(input("Введите массу тела (кг): "))
volume = float(input("Введите объём тела (м³): "))

density = mass / volume
print(f"Плотность материала: {density} кг/м³")
#2.12
print("2.12)")
population = int(input("Введите количество жителей: "))
area = float(input("Введите площадь территории (км²): "))

population_density = population / area
print(f"Плотность населения: {population_density} чел./км²")
#2.13
print("2.13)")
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))

if a != 0:
    x = -b / a
    print(f"Решение уравнения: x = {x}")
else:
    print("Коэффициент a не может быть равен 0!")
#2.14
print("2.14)")
import math

cathetus1 = float(input("Введите первый катет: "))
cathetus2 = float(input("Введите второй катет: "))

hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)
print(f"Гипотенуза: {hypotenuse}")
#2.15
print("2.15)")
import math

R = float(input("Введите внешний радиус: "))
r = float(input("Введите внутренний радиус: "))

area = math.pi * (R**2 - r**2)
print(f"Площадь кольца: {area}")
#2.16
print("2.16)")
import math

cathetus1 = float(input("Введите первый катет: "))
cathetus2 = float(input("Введите второй катет: "))

hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)
perimeter = cathetus1 + cathetus2 + hypotenuse
print(f"Периметр треугольника: {perimeter}")
#2.17
print("2.17)")
import math

base1 = float(input("Введите первое основание: "))
base2 = float(input("Введите второе основание: "))
height = float(input("Введите высоту: "))

# Боковая сторона (используем теорему Пифагора)
side = math.sqrt(height**2 + ((base1 - base2) / 2)**2)
perimeter = base1 + base2 + 2 * side
print(f"Периметр трапеции: {perimeter}")
#2.18
print("2.18)")
import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = (x + (2 + y) / (x ** 2)) / (y + 1 / math.sqrt(x ** 2 + 10))
q = 7.25 * math.sin(x) - abs(y)

print(f"z = {z}")
print(f"q = {q}")
#2.19
print("2.19)")
import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))

x = ((2 / (a ** 2 + 25)) + b) / (math.sqrt(b) + (a + b) / 2)
y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)

print(f"x = {x}")
print(f"y = {y}")
#2.20
print("2.20)")
import math

e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))

a = math.sqrt(abs(e - 3 / f) ** 3 + g)
b = math.sin(e) + math.cos(h) ** 2
c = 33 * g / (e * f - 3)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
import math

# 2.21
print("2.21)")
e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))
a = (e + f/2) / 3
b = abs(h**2 - g)
c = math.sqrt((g - h)**2 - 3 * math.sin(e))
print(f"a = {a}, b = {b}, c = {c}")

# 2.22
print("2.22)")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
abs_num1, abs_num2 = abs(num1), abs(num2)
arithmetic_mean = (abs_num1 + abs_num2) / 2
geometric_mean = math.sqrt(abs_num1 * abs_num2)
print(f"Среднее арифметическое модулей: {arithmetic_mean}, среднее геометрическое: {geometric_mean}")

# 2.23
print("2.23)")
a = float(input("Введите длину первой стороны прямоугольника: "))
b = float(input("Введите длину второй стороны прямоугольника: "))
perimeter = 2 * (a + b)
diagonal = math.sqrt(a**2 + b**2)
print(f"Периметр: {perimeter}, диагональ: {diagonal}")

# 2.24
print("2.24)")
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
print(f"Сумма: {x + y}, разность: {x - y}, произведение: {x * y}, частное: {x / y}")

# 2.25
print("2.25)")
a, b, c = float(input("Введите длину: ")), float(input("Введите ширину: ")), float(input("Введите высоту: "))
volume = a * b * c
side_area = 2 * (a * b + a * c + b * c)
print(f"Объём: {volume}, площадь боковой поверхности: {side_area}")

# 2.26
print("2.26)")
x1, y1 = float(input("Координаты первой точки x: ")), float(input("Координаты первой точки y: "))
x2, y2 = float(input("Координаты второй точки x: ")), float(input("Координаты второй точки y: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Расстояние между точками: {distance}")

# 2.27
print("2.27)")
a, b, h = float(input("Введите длину большего основания: ")), float(input("Введите длину меньшего основания: ")), float(input("Введите высоту: "))
side = math.sqrt(h**2 + ((a - b)/2)**2)
perimeter = a + b + 2 * side
print(f"Периметр трапеции: {perimeter}")

# 2.28
print("2.28)")
a, b, angle = float(input("Введите длину большего основания: ")), float(input("Введите длину меньшего основания: ")), float(input("Введите угол при большем основании (в градусах): "))
h = (a - b) / 2 * math.tan(math.radians(angle))
area = (a + b) * h / 2
print(f"Площадь трапеции: {area}")

# 2.29
print("2.29)")
x1, y1 = float(input("Координаты первой вершины x: ")), float(input("Координаты первой вершины y: "))
x2, y2 = float(input("Координаты второй вершины x: ")), float(input("Координаты второй вершины y: "))
x3, y3 = float(input("Координаты третьей вершины x: ")), float(input("Координаты третьей вершины y: "))
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
perimeter = a + b + c
p = perimeter / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Периметр треугольника: {perimeter}, площадь: {area}")

# 2.30
print("2.30)")
x1, y1 = float(input("Координаты первой вершины четырёхугольника x: ")), float(input("Координаты первой вершины y: "))
x2, y2 = float(input("Координаты второй вершины x: ")), float(input("Координаты второй вершины y: "))
x3, y3 = float(input("Координаты третьей вершины x: ")), float(input("Координаты третьей вершины y: "))
x4, y4 = float(input("Координаты четвёртой вершины x: ")), float(input("Координаты четвёртой вершины y: "))

# Разбиваем четырёхугольник на два треугольника: (x1,y1), (x2,y2), (x3,y3) и (x1,y1), (x3,y3), (x4,y4)
a1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b1 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c1 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
p1 = (a1 + b1 + c1) / 2
area1 = math.sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))

a2 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
b2 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
c2 = math.sqrt((x4 - x1)**2 + (y4 - y1)**2)
p2 = (a2 + b2 + c2) / 2
area2 = math.sqrt(p2 * (p2 - a2) * (p2 - b2) * (p2 - c2))

total_area = area1 + area2
print(f"Площадь четырёхугольника: {total_area}")

# 2.31
print("2.31)")
price_candy = float(input("Стоимость 1 кг конфет: "))
price_cookie = float(input("Стоимость 1 кг печенья: "))
price_apple = float(input("Стоимость 1 кг яблок: "))
kg_candy = float(input("Количество кг конфет: "))
kg_cookie = float(input("Количество кг печенья: "))
kg_apple = float(input("Количество кг яблок: "))
total_cost = price_candy * kg_candy + price_cookie * kg_cookie + price_apple * kg_apple
print(f"Стоимость всей покупки: {total_cost}")

# 2.32
print("2.32)")
monitor_price = float(input("Стоимость монитора: "))
system_unit_price = float(input("Стоимость системного блока: "))
keyboard_price = float(input("Стоимость клавиатуры: "))
mouse_price = float(input("Стоимость мыши: "))
total_pc_cost = monitor_price + system_unit_price + keyboard_price + mouse_price
n = int(input("Количество компьютеров: "))
total_cost = total_pc_cost * n
print(f"Стоимость {n} компьютеров: {total_cost}")

# 2.33
print("2.33)")
x = float(input("Возраст Тани (X лет): "))
y = float(input("Возраст Мити (Y лет): "))
avg_age = (x + y) / 2
diff_x = abs(x - avg_age)
diff_y = abs(y - avg_age)
print(f"Средний возраст: {avg_age}, разница возраста Тани со средним: {diff_x}, разница возраста Мити со средним: {diff_y}")

# 2.34
print("2.34)")
v1 = float(input("Скорость первого автомобиля (км/ч): "))
v2 = float(input("Скорость второго автомобиля (км/ч): "))
s = float(input("Расстояние между автомобилями (км): "))
t = s / (v1 + v2)
print(f"Время до встречи: {t} часов")

# 2.35
print("2.35)")
v1 = float(input("Скорость первого автомобиля (км/ч): "))
v2 = float(input("Скорость второго автомобиля (км/ч): "))
s = float(input("Начальное расстояние между автомобилями (км): "))
t = 0.5  # 30 минут = 0.5 часа
distance_after_30min = s + (v1 - v2) * t
print(f"Расстояние между автомобилями через 30 минут: {distance_after_30min} км")