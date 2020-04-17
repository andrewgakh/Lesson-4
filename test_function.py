# Тестирование функции F

from Homework4 import F

# Длина списка 100, результат Passed
def test_1_F():
    n = 100
    x = ['Николай', 'Галина', 'Евгения', 'Иван', 'Михаил', 'Ольга', 'Александр', 'Фаина', 'Татьяна','Светлана',
                  'Олег','Анна', 'Андрей', 'Сергей', 'Леонид', 'Юрий', 'Палина', 'Степан', 'Дмитрий', 'Оксана']
    assert len(F(n, x)) == 100

# Две строки из 10 имен не совпадают, результат FAiled
def test_2_F():
    n = 10
    x = ['Николай', 'Галина', 'Евгения', 'Иван', 'Михаил', 'Ольга', 'Александр', 'Фаина', 'Татьяна', 'Светлана',
         'Олег', 'Анна', 'Андрей', 'Сергей', 'Леонид', 'Юрий', 'Палина', 'Степан', 'Дмитрий', 'Оксана']
    assert F(n,x) == ['Оксана', 'Сергей', 'Евгения', 'Анна', 'Олег', 'Анна', 'Анна', 'Юрий', 'Татьяна', 'Николай']