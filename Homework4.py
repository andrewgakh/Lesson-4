# Задача 1.
# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из
# первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется
# использовать функцию random);
#
# Задача 2.
# Напишите функцию вывода самого частого имени из списка на выходе функции F;
# Задача 3.
# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
#**********************************************************************************************************************
import random
from random import randint

def F (n, x):
    '''
    :param n: Длина нового списка имен
    :param x: Список имен
    :return: Список длины n  случайных имен из списка x
    '''
    list_2 = []
    i = 0

    for i in range(n):
        k=randint(0,19)
        list_2.append(x[k])
        global name_list
        name_list = list_2
    return print(list_2)

def FF(x):
    '''
    :param x: Список имен
    :return: Самое частое имя в списке x
    '''

    global name_list
    j = 0
    i = 0
    kol = 1
    dict_words = {}
    dlina = len(x)

    while i < (len(x) - 1):

        if (i) < len(x) and x[i] == '':
            i = i + 1
        else:
            i = i + 0

        j = i + 1
        while j < len(x):
            if x[i] == x[j]:
                kol+= 1
                x[j] = ''
            j+= 1
        dict_words[x[i]] = kol
        kol = 1
        i = i + 1
    i = 0
    ii = 0
    list_d = list(dict_words.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    print('Список имен отсортирован по возрастанию')
    print(list_d)
    print()
    for i in list_d:
        if ii < 1:
            name_often = i[0]
        else: break
        ii+= 1
    return print ( 'Наиболее часто встречающееся имя в списке:  ', name_often)

list_name1 = ['Николай', 'Галина','Евгения','Иван','Михаил', 'Ольга','Александр','Фаина','Татьяна','Светлана','Олег',
              'Анна','Андрей','Сергей','Леонид','Юрий','Палина','Степан','Дмитрий','Оксана']
name_list = []

print()
print('Задача 1.')
print()

nn=int(input('Введите целое число '))

print('Новый список имен: ')
F(nn, list_name1)

print()
print('Задача 2. ')
FF(name_list)
#print(name_list)