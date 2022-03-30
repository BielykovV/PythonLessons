a = int(input('Triangle height: '))
for i in range(a):  # а = количество раз выполнения цикла, т.е. кол-во строк
    n1 = a - (i + 1)  # количество пробелов с начала каждой строки
    n2 = a + i  # длина каждой строки в цикле
    for j in range(n2):
        print('*' if j >= n1 else ' ', end='')
    print('')
