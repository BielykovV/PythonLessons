a = int(input('Triangle height: '))
for i in range(a):  # а = количество раз выполнения цикла, т.е. кол-во строк
    if i == (a - 1):
        print('*' * (a + i))
        break
    n1 = a - (i + 1)  # количество пробелов с начала каждой строки
    n2 = a + i  # длина каждой строки в цикле
    for j in range(n2):
        if j == n1:
            print('*', end='')
        elif j == (n2 - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
