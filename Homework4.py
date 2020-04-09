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

    # j = 0
    # i = 0
    # kol = 1
    # dict_words = {}
    # dlina = len(x)
    print('Наиболее часто встречающееся имя в списке:  ')
    dict_tmp(x,True)

    # while i < (len(x) - 1):
    #
    #     if (i) < len(x) and x[i] == '':
    #         i = i + 1
    #     else:
    #         i = i + 0
    #
    #     j = i + 1
    #     while j < len(x):
    #         if x[i] == x[j]:
    #             kol+= 1
    #             x[j] = ''
    #         j+= 1
    #     dict_words[x[i]] = kol
    #     kol = 1
    #     i = i + 1
    # i = 0
    # ii = 0
    # # list_d = list(dict_words.items())
    # # list_d.sort(key=lambda i: i[1], reverse=True)
    # list_d = list(dict_tm.items())
    # list_d.sort(key=lambda i: i[1], reverse=True)
    # print('Список имен отсортирован по возрастанию')
    # print(list_d)
    # print()
    # for i in list_d:
    #     if ii < 1:
    #         name_often = i[0]
    #     else: break
    #     ii+= 1
    # return print ( 'Наиболее часто встречающееся имя в списке:  ', name_often)
    return


def dict_tmp(x, y):
    '''
    :param x: Входной список
    :param y: Логический переключатель True/False. Упорядочивает  список по убыванию/возрастанию.
    :return: Возвращает наиболее/наименее встречающийся элемент списка
    '''
    #global dict_tm
    # j = 0
    # i = 0
    # kol = 1
    dict_words = {}
    # dlina = len(x)
    # Определяем как часто слово встречается в списке, создаем словарь
    for i in range(len(x)):
        #dict_words
        dict_words[x[i]] = x.count(x[i])

    # Сортируем словарь согласно логической переменной
    list_d = list(dict_words.items())
    print(list_d)
    list_d.sort(key=lambda i: i[1], reverse=y)
    print(list_d)
    oft = list(list_d[0])

    # while i < (len(x) - 1):
    #
    #     if (i) < len(x) and x[i] == '':
    #         i = i + 1
    #     else:
    #         i = i + 0
    #
    #     j = i + 1
    #     while j < len(x):
    #         if x[i] == x[j]:
    #             kol += 1
    #             x[j] = ''
    #         j += 1
    #     dict_words[x[i]] = kol
    #     kol = 1
    #     i = i + 1
    #dict_tm = dict_words
    return print (oft[0])

def FFF(x):
    '''
    :param x: Список имен
    :return: Самая редкая буква, с которой начинается имя в списке x
    '''

    j = 0
    i = 0
    kol = 1
    bukva = []
    tmp = []
    bukva_sld = []
    dict_words = {}
    dlina = len(x)

    for i in range (len(x)):
        tmp = list(x[i])
        bukva.append(tmp[0])
    print('bukva = ', bukva)

    j = 0
    i = 0
    while i < (len(bukva) - 1):

        if i < len(bukva) and x[i] == '':
            i = i + 1
        else:
            i = i + 0

        j = i + 1
        while j < len(bukva):
            if bukva[i] == bukva[j]:
                kol += 1
                bukva[j] = ''
            j += 1
        dict_words[bukva[i]] = kol
        kol = 1
        i = i + 1
    i = 0
    ii = 0
    list_d = list(dict_words.items())
    print(list_d)
    list_d.sort(key=lambda i: i[1], reverse=False)
    for i in list_d:
        if ii < 1:
            bukva_sld = i[0]
        else:
            break
        ii += 1
    print ('Самая редкая буква, с которой начинается имя в списке')
    return print(bukva_sld)

list_name1 = ['Николай', 'Галина','Евгения','Иван','Михаил', 'Ольга','Александр','Фаина','Татьяна','Светлана','Олег',
              'Анна','Андрей','Сергей','Леонид','Юрий','Палина','Степан','Дмитрий','Оксана']

# Результат функции F(x)
name_list = []
dict_tm={}

print()
print('Задача 1.')
print()

nn=int(input('Введите целое число '))

print('Новый список имен: ')
F(nn, list_name1)

print()
print('Задача 2. ')
FF(name_list)

# print()
# print('Задача 3. ')
# FFF(name_list)
# #print(name_list)