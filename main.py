print("2.36)")
celsius = float(input("Введите температуру по шкале Цельсия: "))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
print(f"Температура по шкале Фаренгейта: {fahrenheit:.2f}°F")
print(f"Температура по шкале Кельвина: {kelvin:.2f}K")

print("2.37)")
fahrenheit_fixed = 450
celsius_from_fahrenheit = (fahrenheit_fixed - 32) / 1.8
print(f"450°F соответствует {celsius_from_fahrenheit:.2f}°C")

print("2.38)")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
average = (num1 + num2) / 2
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient:.6f}")
print(f"Среднее арифметическое: {average:.6f}")
