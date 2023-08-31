
# 22.08.23

# создание списка
list_3 = []
list_1 = list()
list_2 = [1, 2, 3]
print(list)
print(list_1)
print(list_2)
print(*list_2)
for i in list_2:
    print(i)

print(len(list_2))
print(list_2[0])
print(list_2[-1]) #индексация с конца списка

list_2.append(8) #добавление в конец списка
print(list_2)

list_4 = []
for i in range(5): #наполняем значениями наш список от 1 и до 5, i = 0,1,2,3,4,
    list_4.append(i)
    print(list_4)

    #удаление последнего элемента списка
list_5 = [12, 5, 2, -6, 4]
print(list_5)
print(list_5.pop()) #удаляем 4 последний элемент
print(list_5)

# удаление конкретного элемента списка
print(list_5.pop(0)) #удаляем 0 элемент в списке = 12
print(list_5)

# добавляем элемент на нужную позицию
print(list_5.insert(2, 14)) #добавдяем на 2 позицию значение 14
print(list_5)
list_6 = [1,2,5,7,34,2]
print(list_6[len(list_6)-1]) #печать 1 элемент с конца длинны списка = 2
print(list_6[len(list_6)-2:])#печать 2х элемент с конца длинны списка = 34,2
print(list_6[:])#печать всех элементов с начала списка
print(list_6[::3])#печать с начала и 6й элемент 1,7
print(list_6[::3])#печать с начала и 6й элемент 1,7
print(list_6[1:3])#печать от 1 и до 3 элемента 2,5
print(list_6[2:-18])#печать от 2 до -18 с конца, такого пересечения нет результат []
print(list_6[1:len(list_6):3])#печать c 1 элемента и до конца с шагов 3 = 2,34

#Кортежи
t = ()
print(type(t))
t = (1)
print(type(t))
t = (1, 2, ) # для записи значения в кортеж необходимо в конце писать ","

v = [1, 2, 3]
print(type(v))
print(v)
v = tuple(v)
print(type(v))
print(v)
a, b, c = v
print(a, b, c)

for i in v:
    print(i)
for i in range(len(v)):
    print(v[i])

i = 0
while i < 5:
    if i == 3:
        break#лучше не использовать
    i = i + 1
else:
    print("пожалуй")
    print("хватит)")
print(i)

#метод флага поиск мнимального делителя
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i +=1
# range (1,6,2) = генерим значения от куда начинаем, где заканчиваем и шаг
# range (5) генерим значения от 0 о числа в скобках не включая его

line = ""
for i in range(5):
    line = ""
    for j in range(5):#не работает
        line = "*"
        print(line)

# print (i, end = " ") список распечатается с разделителями
# print (end = "\n") перенос печати на новую строку

sp = [1, 3, [1,3,4,], "sss", "mmm"]
for el in sp:
    print(el, end = "")
print (end = "\n")
for item in enumerate():
    print(item)
a = 'arakadabra'
p = set('arakadabra') # убираем дубли
print(p)
#словари
my_direct = {None: {1:a}, 2:240, "g":4}
print(my_direct[2])
my_direct[2] = 400
print(my_direct.keys())
print(my_direct.items())
for k,v in my_direct.items():
    print(k,v)



