#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# 1.2
from sys import argv

name, time, salary, bonus = argv
try:
    print(argv)
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = time * salary + bonus
    print(f'Заработная плата сотрудника {result}')
except ValueError:
    print('Not a number')
