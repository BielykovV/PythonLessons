import random
height = [random.randint(160, 200) for _ in range(5)]
height.sort()
petya = [int(input())]
if petya[0] in height:
    height.insert(height.index(petya[0]), petya[0])
else:
    height.append(petya[0])
print(height)  # строка для проверки
petya_position = ((len(height)) - height.index(petya[0]))
print(petya_position)



