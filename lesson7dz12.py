def aritmetrhic(int_1=int(input('Первое число: ')),
                int_2=int(input('Второе число: ')), opr=input('Операция ')):
    """
    Function takes from user three args: 1, 2 - int, 3 - operation (+-/*)
    Function gives the result of taken operation between 1st and 2nd args
    :param int_1:
    :param int_2:
    :param opr: only +-/*
    :return:
    """
    if opr == '+':
        print(int_1+int_2)
    elif opr == '-':
        print(int_1-int_2)
    elif opr == '*':
        print(int_1*int_2)
    elif opr == '/':
        print(int_1/int_2)
    else:
        print('Неизеветсная операция')


if __name__ == '__main__':
    aritmetrhic()
