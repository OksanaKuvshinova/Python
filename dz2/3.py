#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение c помощью списка
month = int(input("Введите номер месяца от 1 до 12: "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tНомер введен некорректно! Введите номер от 1 до 12.")
        month = int(input("Введите номер месяца от 1 до 12: "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tВведенный месяц относится к времени года - '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tВведенный месяц относится к времени года - '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tВведенный месяц относится к времени года - '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tВведенный месяц относится к времени года - '{mlist[3]}'")
        break

# Решение c помощью словаря
# month = int(input("Введите номер месяца от 1 до 12: "))
#
# seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
# months_dict = {1: seasons.get(1), 2: seasons.get(1), 3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
              # 6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3), 9: seasons.get(4), 10: seasons.get(4),
              # 11: seasons.get(4), 12: seasons.get(1)}
# value = months_dict[month] if month in months_dict else print(f"Месяц с номером {month} не существует")
# print(f"\tВведенный месяц относится к времени года - {month} - '{value}'")

