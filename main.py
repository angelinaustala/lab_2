def ypr1():
    a = input("Введите пароль: ")
    b = input("Повторите пароль: ")

    if a.islower():
        message = "Пароль должен содержать хотя бы один большой символ."
        print(message)
    elif b.islower():
        message = "Повторите пароль с одним большим символом."
        print(message)

    elif a != b:
        message = "Пароли не совпадают."
        print(message)
    else:
        message = "Пароль принят!"
        print(message)
ypr1()

def ypr2():
    n = int(input('Введите номер места'))

    if n % 2 == 0 and n <= 36:
        print('Вверхнее место в купе')
    elif n % 2 != 0 and n <= 35:
        print('Нижнее место в купе')
    elif n % 2 == 0 and n > 36:
        print('Вверхнее боковое место')
    elif n % 2 != 0 and n <= 53:
        print('Нижнее боковое место')
    else:
        print("Ошибка")

ypr2()

def ypr3():
    year = int(input('Введите год: '))

    if year % 4 != 0:
        print('Год не високосный.')

    elif year % 100 == 0:
        if year % 400 == 0:
            print('Год високосный.')
        else:
            print('Год не високосный.')
    else:
        print('Год високосный.')

ypr3()

def ypr4():
    a = input('Введите цвет 1: ')
    b = input('Введите цвет 2: ')
    if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('фиолетовый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('оранжевый')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('зеленый')
    elif a == 'синий' and b == 'синий':
        print('синий')
    else:
        print('ошибка цвета')
ypr4()