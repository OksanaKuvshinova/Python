# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divizion(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Dividing by zero is not allowed'

print(divizion((int(input('Enter first number: '))), (int(input('Enter second number: ')))))
