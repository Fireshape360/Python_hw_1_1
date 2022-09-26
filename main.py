print("Введите номер дня недели")

weekday = int(input())

if weekday > 7:
    print("Неверные данные")
else:
    if weekday == 6 or weekday == 7:
        print("Это выходной день")
    else:
        print("Это будний день")
