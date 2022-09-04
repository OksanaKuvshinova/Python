# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

new_number = int(input("Введите новый элемент рейтинга: "))
rating_list = [7, 4, 3, 2]
c = rating_list.count(new_number)
for element in rating_list:
    if c > 0:
        i = rating_list.index(new_number)
        rating_list.insert(i+c, new_number)
        break
    else:
        if new_number > element:
            j = rating_list.index(element)
            rating_list.insert(j, new_number)
            break
        elif new_number < rating_list[len(rating_list) - 1]:
            rating_list.append(new_number)
print(rating_list)