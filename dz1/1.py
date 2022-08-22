# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


a = 5
b = 6
print(a, b)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = float(input("Enter your favourite number: "))
print("Привет, {}! Тебе уже {} лет! А твое любимое число - {}.". format(name, age, number))

