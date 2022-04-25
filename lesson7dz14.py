def work(a=int(input('Введите любое целое число: '))):
    """
    Func takes int and gives work of it's all numbers without '0'.
    If given int == 0, gives 0.
    :param a: any int
    :return:
    """
    numbers = list(str(a))
    res = 1
    if a != 0:
        for i in numbers:
            if int(i) != 0:
                res *= int(i)
        print(f'Произведение цифр:{res}')
    else:
        print('0')


if __name__ == '__main__':
    work()
