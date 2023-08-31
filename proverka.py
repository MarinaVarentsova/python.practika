from random import randint
list1_set = set(randint(1, 10) for i in range(int(input("введите количество элементов 1 списка: "))))
print(list1_set)
list2_set = set(randint(1, 10) for i in range(int(input("введите количество элементов 2 списка: "))))
print(list2_set)
list3_set = sorted(list1_set.intersection(list2_set))
print(list3_set)
