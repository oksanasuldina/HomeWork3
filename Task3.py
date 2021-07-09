def my_func(arg1, arg2, arg3):
    tuple_args = (arg1, arg2, arg3)
    return sum(tuple_args) - min(tuple_args)


menu = 1
while menu != 0:
    number1 = int(input('число 1 '))
    number2 = int(input('число 2 '))
    number3 = int(input('число 3 '))
    print('сумма наибольших двух аргументов: {}'.format(my_func(number1, number2, number3)))
    menu = int(input('1 - продолжить, 0 - завершить '))
