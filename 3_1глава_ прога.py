print("3.1)")
cm = float(input("Введите расстояние в сантиметрах: "))
meters = int(cm // 100)
print(f"Число полных метров: {meters}")

print("3.2)")
kg = float(input("Введите массу в килограммах: "))
centners = int(kg // 100)
print(f"Число полных центнеров: {centners}")

print("3.3)")
days = 234
weeks = int(days // 7)
print(f"Полных недель: {weeks}")

print("3.4)")
N = int(input("Введите количество школьников (N): "))
k = int(input("Введите количество яблок (k): "))
apples_per_student = k // N
remaining_apples = k % N
print(f"Каждому школьнику достанется {apples_per_student} яблок.")
print(f"В корзинке останется {remaining_apples} яблок.")

print("3.5)")
width = 543
height = 130
square_side = 130
squares_width = width // square_side
squares_height = height // square_side
total_squares = squares_width * squares_height
print(f"Можно отрезать {total_squares} квадратов.")

print("3.6)")
total_seats_per_compartment = 4
seat_number = int(input("Введите номер места: "))
compartment_number = (seat_number - 1) // total_seats_per_compartment + 1
print(f"Место находится в купе №{compartment_number}")

print("3.7)")
total_apartments = 15
floors = 5
apartment_number = int(input("Введите номер квартиры: "))
floor_number = (apartment_number - 1) // (total_apartments // floors) + 1
print(f"Квартира находится на {floor_number} этаже.")

print("3.8)")
seats_per_row = 15
ticket_number = int(input("Введите серийный номер билета: "))
row_number = (ticket_number - 1) // seats_per_row + 1
print(f"Место находится в ряду №{row_number}")

print("3.9)")
n = int(input("Введите количество секунд с начала суток: "))
hours = n // 3600
minutes = (n % 3600) // 60
seconds = n % 60
print(f"Полных часов: {hours}")
print(f"Полных минут с начала часа: {minutes}")
print(f"Полных секунд с начала минуты: {seconds}")
