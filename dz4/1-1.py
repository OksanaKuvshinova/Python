#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# 1.1
def salary_all():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в час '))
        bonus = int(input('Премия '))
        result = time * salary + bonus
        print(f'Заработная плата сотрудника {result}')
    except ValueError:
        return print('Not a number')
salary_all()

