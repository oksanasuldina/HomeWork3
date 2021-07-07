result = 0
menu = 1
while menu != 0:
    if menu != 5:
        numbers = input('введите строку чисел через пробел ').split()
        number_list = list(numbers)
        for i in range(0, len(number_list), 1):
            result += int(number_list[i])
            i += 1
        print('сумма чисел: {}'.format(result))
        menu = int(input('1 - продолжить, 5 - добавить сумму и завершить, 0 - завершить '))
    else:
        numbers = input('введите строку чисел через пробел ').split()
        number_list = list(numbers)
        for i in range(0, len(number_list), 1):
            result += int(number_list[i])
            i += 1
        print('сумма чисел: {}'.format(result))
        menu = 0
