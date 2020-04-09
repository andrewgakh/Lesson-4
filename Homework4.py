# Задача 1.
# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из
# первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется
# использовать функцию random);
#
# Задача 2.
# Напишите функцию вывода самого частого имени из списка на выходе функции F;
#
# Задача 3.
# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F;
#
# Задача 4.
#  В файле с логами найти дату самого позднего лога (по метке времени)
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

def dict_tmp(x, y):
    '''
    :param x: Входной список
    :param y: Логический переключатель True/False. Упорядочивает  список по возрастанию/убыванию.
    :return: Возвращает наиболее/наименее встречающийся элемент списка
    '''

    dict_words = {}

    # Определяем как часто слово встречается в списке, заполняем словарь.
    for i in range(len(x)):
        dict_words[x[i]] = x.count(x[i])

    # Сортируем словарь согласно логической переменной.
    list_d = list(dict_words.items())
    print(list_d)
    list_d.sort(key=lambda i: i[1], reverse=y)
    print(list_d)
    oft = list(list_d[0])

    return print (oft[0])


list_name1 = ['Николай', 'Галина','Евгения','Иван','Михаил', 'Ольга','Александр','Фаина','Татьяна','Светлана','Олег',
              'Анна','Андрей','Сергей','Леонид','Юрий','Палина','Степан','Дмитрий','Оксана']

list_log=['2011-08-01 18:03:34,338 - exampleApp - INFO - Program started',
          '2012-09-02 19:13:53,338 - exampleApp - INFO - added 7 and 8 to get15',
          '2012-10-02 20:23:31,338 - exampleApp - INFO - Done!',
          '2013-08-01 01:43:33,338 - exampleApp - INFO - Program started',
          '2011-09-19 12:53:33,338 - exampleApp - INFO - added 10 and 11 to get15',
          '2012-10-12 22:03:33,338 - exampleApp - INFO - Done!',
          '2017-08-01 01:13:51,338 - exampleApp - INFO - Program started',
          '2019-09-19 12:21:34,338 - exampleApp - INFO - added 7 and 8 to get15',
          '2019-09-19 12:51:34,338 - exampleApp - INFO - added 7 and 8 to get15',
          '2018-10-12 23:31:01,338 - exampleApp - INFO - Done!']

name_list = [] # Результат функции F(x)
dict_tm={}
tmp=[]
tmp1=[]
bukva=[]

print()
print('Задача 1.')
print()

nn=int(input('Введите целое число '))

print('Новый список имен: ')
F(nn, list_name1)

print()
print('Задача 2. ')
print('Наиболее часто встречающееся имя в списке:  ')
dict_tmp(name_list,True)


print()
print('Задача 3. ')

# Подготовим список состоящий из первых букв имен списка, результат функции F(x).
for i in range(len(name_list)):
    tmp = list(name_list[i])
    bukva.append(tmp[0])

print('Cамая редкая буква, с которой начинаются именя в списке')
dict_tmp(bukva,False)

print()
print('Задача 4. ')

# Отсортирует лог файл, по возрастанию, по году, дате.
tmp.clear()
for i in range (len(list_log)):
    tmp.append( list_log[i].split())


tmp.sort(key=lambda i: i[0]+' '+i[1], reverse=True)
print('Cообщения из лог.файла упорядочены по времени : ')
print(tmp)
print()
print('Последнее сообщение из лог.файла: ')
print(tmp[0])
