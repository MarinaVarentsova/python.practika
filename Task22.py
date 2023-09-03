# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
n = int(input("введите количество элементов 1 списка: "))
m = int(input("введите количество элементов 2 списка: "))
list1 = [randint(0, 10) for i in range(n)]
list2 = [randint(0, 10) for i in range(m)]
print(list1, end=" ")
print("\n")
print(list2, end=" ")

list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            temp = list1[i]
            list3.append(temp)
        else:
            j +=1
    i +=1
print("\n")
print(sorted(set(list3)))