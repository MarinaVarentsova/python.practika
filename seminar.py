import random
from random import randint
import time
def show_test():
    print(randint(1, 10))
    print(time.time())

show_test()

# для задного числа n выведите N! т.е. произвдедение всех числе от 1 до N
n = int(input("введите число n: "))
i = 1
sum = 1
while i < n:
    sum = sum * i
    i += 1
# print(sum)

def fact(n):
    i = 1
    result = 1
    while i < n:
        result *= i
        i += 1
    return result
n = int(input("введите число n: "))
print(fact(n))



#опредледить является ли число n последовательностью фибоначи и каким по счету
def fibonachi(n):
    n1 = 0
    n2 = 1
    counter = 2
    result = 0
    while result < n:
        result = n2 + n1
        n1 = n2
        n2 = result
        counter += 1
    if n == 0:
        return 1
    if n == 1:
        return 2
    if result == n:
        return counter
    else:
        return (f"n - не число Фибоначи + предыдущее число Фибоначи к n {n1}")

try:
    n = int(input("введите число n: "))
    print(fibonachi(n))
except:
    print("неверный формат n, введите число")


#определить сколько была сама длинная оттепель (погода больше 0)
def ottepel(n):
    counter = 1
    max_day = 0
    for i in range(n):
        temperatura = random.randrange(-50, 50)
        print(temperatura, end = " ")
        if temperatura > 0:
            if max_day < counter:
                max_day = counter
            counter +=1
        else:
            counter = 1

    print(end= "\n")
    return max_day

n = int(input("введите число n: "))
print(ottepel(n), end = "\n")

#определения мин и макс
def minMax(n):
    max = 1
    for i in range(n):
        counter = random.randrange(1, 15)
        print(counter, end = " ")
        min = counter
        if counter > max:
            max = counter
        if counter < min:
            min = counter
        counter +=1
    print(end= "\n")
    return max, min

n = int(input("введите число n: "))
print(minMax(n), end = "\n")

#определение сколько уникальных чисел в списке
list_1 = [1, 2, -3, 5, 3, -2, 5]
list_2 = set(list_1)
print(len(list_2))
#дана последоватлеьность, необходимо ее сдвинуть вправо шаг K
list_1=[1,2,3,4,5]
k=3
i = 0
for i in range(len(list_1)-1):
    list_1[i] = list[i] + k
    i+=1

print(list_1)

#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
list_1 = [1, 2, 3, 323, 5]
k = 3
j=0
for i in range(len(list_1)):
    if list_1[i] == k:
       j+=1
       i+=1
    else:
       i+=1
print(j)

#Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [6, 2, 5, 3]
k = 4
n = abs(k - list_1[0])
min = list_1[1]

for i in range(len(list_1)):
    temp = k - list_1[i]
    abstemp = abs(temp) #модуль разницы
    if abstemp < n:
        n = abstemp
        min = list_1[i]
        i += 1
    else:
        i += 1

print(min)


#  Напишите программу, которая принимает на вход
#  строку, и отслеживает, сколько раз каждый символ
#  уже встречался. Количество повторов добавляется к
#  символам с помощью постфикса формата _n.
#  Input: a a a b c a a d c d d
#  Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#  Для решения данной задачи используйте функцию
#  .split()

def Get_Count_Letter(sp):
    sp1 = sp.split()
    lib = {}
    sp_out = []
    for i in sp1:
        if i in lib:
            sp_out.append(i + "_" + str(lib[i]))
            lib[i] = lib[i] + 1
        else:
            lib[i] = 1
            sp_out.append(i)
    return sp_out


sp = "a a a b c a a d c d d"
print(Get_Count_Letter(sp))

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

list_rus = {1:"А, В, Е, И, Н, О, Р, С, Т",
            2:"Д, К, Л, М, П, У",
            3:"Б, Г, Ё, Ь, Я",
            4:"Й, Ы ",
            5:"Ж, З, Х, Ц, Ч",
            8:"Ш, Э, Ю",
            10:"Ф, Щ, Ъ"}
list_en = {1:"A, E, I, O, U, L, N, S, T, R",
           2:"D, G",
           3:"B, C, M, P",
           4:"F, H, V, W, Y",
           5:"K",
           8:"J, X",
           10:"Q, Z"}

n = input("введите К")
h = n.upper()
sum = 0
for i in h:
    for k,v in list_en.items():
        if i in v:
            sum = sum + k
    for k,v in list_rus.items():
        if i in v:
            sum = sum + k
print(sum)