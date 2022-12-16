# (Семинар 2, Задача 1)
# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81
# (для N = 5: 1*(-3), -3*(-3), 9*(-3), 27*(-3))

################
# НОВОЕ РЕШЕНИЕ
################

n = int(input('Введите число: '))

# через map, lambda и генератор списка:
nums = list(map(lambda e: (-3)**e, [i for i in range(n)]))

print(f'{n} -> {nums}')


################
# СТАРОЕ РЕШЕНИЕ
################
# 
# n = int(input('Введите число: '))
# print(f'n = {n}: ',end='')

# for i in range(n):
#     if i == n-1:
#         print((-3)**i)
#     else:
#         print((-3)**i, end=', ')