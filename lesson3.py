print('Введите что нибудь')
a = input('')
b = 'Это строка в которую '
c = ' в новую строку'
print(b+a+c)
a = 'замена в строке'
print(b+a+c)
print(len(b+a+c))
if (b+a+c).find('строка') < 0:
    print('Нет')
else:
    print('Да')
