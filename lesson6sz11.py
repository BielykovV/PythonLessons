import random
import string

v_1 = str(random.randint(1000, 9999))  # list of ints not less 4 symbols
k_1 = [random.choice(string.ascii_letters) for _ in
       range(random.randint(4, len(v_1)))]
# произвольно взял не более 4 ключей для словаря
dict_1 = {k_1[i]: v_1[i] for i in range(len(k_1))}

v_2 = str(random.randint(1000, 9999))
k_2 = [random.choice(string.ascii_letters) for _ in
       range(random.randint(4, len(v_2)))]
dict_2 = {k_2[i]: v_2[i] for i in range(len(k_2))}

print(dict_1)
print(dict_2)
print(dict_1.keys())
print(dict_2.keys())  # строки для проверки

for k in dict_2.keys():
    dict_1.setdefault(k, (dict_2[k]))
    if dict_2[k] > dict_1[k]:
        dict_1[k] = dict_2[k]
print(dict_1)
