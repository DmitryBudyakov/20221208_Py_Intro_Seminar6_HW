# (Семинар 3, ДЗ Задача 1)
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.  
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Сумма элементов на нечетных позициях'
print('-'*len(title))
print(title)
print('-'*len(title))

# тестовый список
# nums = [2, 3, 5, 9, 3]

###############
# НОВОЕ РЕШЕНИЕ
###############

num = int(input('Введите сколько будет чисел в списке: '))
nums = [randint(1,10) for i in range(num)]

# с использованием enumerate и генератора списка:
sum_odd = sum([v for k,v in enumerate(nums) if k % 2 != 0])

print(f'{nums} -> сумма на нечетных позициях = {sum_odd}')


#################
# СТАРОЕ РЕШЕНИЕ
#################
# 
# def create_random_int_list(n: int) -> list:
#     min_n, max_n = 1, 10
#     int_list = [randint(min_n, max_n) for i in range(n)]
#     return int_list

# num = int(input('Введите сколько будет чисел в списке: '))
# nums = create_random_int_list(num)

# sum_elems = 0
# for i in range(len(nums)):
#     if i % 2 != 0:
#         sum_elems += nums[i]

# print(f'{nums} -> сумма на нечетных позициях = {sum_elems}')
