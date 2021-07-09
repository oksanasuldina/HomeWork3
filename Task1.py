def division(div1, div2):
    return round(div1 / div2, 2)


menu = 1
while menu != 0:
    divisible = int(input('делимое '))
    divisor = int(input('делитель '))
    if divisor == 0:
        print('Division by zero')
        menu = int(input('1 - продолжить, 0 - завершить '))
    else:
        print('частное = {}'.format(division(divisible, divisor)))
        menu = int(input('1 - продолжить, 0 - завершить '))
