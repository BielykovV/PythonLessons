import random
random_list_1 = [random.randint(0, 10) for _ in range(10)]
# в задаче не указана длина строки которая дана, взял 10
random_list_2 = [random.randint(0, 10) for _ in range(10)]
uniq_list = []
print(random_list_1)
print(random_list_2)
for i in random_list_1:
    if i in random_list_2:
        if i not in uniq_list:
            uniq_list.append(i)
print(uniq_list)  # создал строку для удобства проверки
print(len(uniq_list))
