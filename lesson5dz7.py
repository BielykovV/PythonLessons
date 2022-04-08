import random
rnd_list = [random.randint(0, 10) for _ in range(10)]
print(rnd_list)  # строка для проверки
more_than_neighbors = 0
for i in range(0, len(rnd_list) - 1):
    if rnd_list[i-1] < rnd_list[i] > rnd_list[i+1]:
        more_than_neighbors += 1
print(more_than_neighbors)
