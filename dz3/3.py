#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a1, a2, a3):
    print(f'Сумма двух наибольших аргументов равна: {a1 + a2 + a3 - min([a1, a2, a3])}')

my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)