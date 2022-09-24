# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

# float_num = input('Введите чило: ')
#   print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

#N = int(input())
#fact = 1 
#some_list = []
#for i in gange(1, N + 1):
#    some_list.append(fact * i)
#    fact *= i
#print(some_list)  


#Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#n = int(input())
#summ = 0
#for i in range(1, n + 1):
#    summ += (1 + 1 / i) ** i 
#print(summ)    

#Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

#from random import *
#n = int(input())

#some_list = [randint(-n, n) for _ in range(randint(5, 10))]
#print(some_list)

#f = open('17.txt', 'w')
#for i in range(randint(2, len(some_list))):
#    f.write(str(randint(0, len(some_list) - 1)) + '\n')
#f.close()

#pr = 1
#with open('17.txt', 'r') as f:
#    for i in f.read().splitlines():
#        pr = pr * some_list[int(i)]
#print(pr)

#Реализуйте алгоритм перемешивания списка.

from random import shuffle

some = [1, 5, 7, 9, 10]
shuffle(some)
print(some)
