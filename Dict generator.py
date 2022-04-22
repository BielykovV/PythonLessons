import random
import string

v_1 = str(random.randint(10000, 99999))  # list of ints not less 5 symbols
k_1 = [random.choice(string.ascii_letters) for _ in
       range(random.randint(5, len(v_1)))]
# произвольно взял 5 ключей для словаря
dict_1 = {k_1[i]: v_1[i] for i in range(len(k_1))}
print(dict_1)

v_2 = str(random.randint(10000, 99999))
k_2 = [random.choice(string.ascii_letters) for _ in
       range(random.randint(5, len(v_2)))]
dict_2 = {k_2[i]: v_2[i] for i in range(len(k_2))}
print(dict_2)
