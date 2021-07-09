def my_func_1(arg1, arg2):
    return arg1 ** arg2


def my_func_2(arg1, arg2):
    i = 2
    degree = x
    while i <= abs(arg2):
        degree = degree * arg1
        i += 1
    return 1 / degree


menu = 1
while menu != 0:
    x = float(input('введите действительное положительное число x '))
    y = int(input("введите целое отрицательное число y "))
    if (x > 0) and (y < 0):
        print('1 способ x в степени у: {}'.format(my_func_1(x, y)))
        print('2 способ x в степени у: {}'.format(my_func_2(x, y)))
        menu = int(input('1 - продолжить, 0 - завершить '))
    elif (x <= 0) or (y > 0):
        print('x должно быть ПОЛОЖИТЕЛЬНЫМ, у - ОТРИЦАТЕЛЬНЫМ')
        menu = int(input('1 - продолжить, 0 - завершить '))
    elif y == 0:
        print('любое число в степени 0 равно 1 x в степени у: 1')
        menu = int(input('1 - продолжить, 0 - завершить '))

