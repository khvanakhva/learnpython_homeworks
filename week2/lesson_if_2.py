# Практика: Сравнение строк
# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты


def str_comp(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    elif len(str1) != len(str2) and str2 == 'learn':
        return 3
    elif str1 != str2 and len(str1) > len(str2):
        return 2
    elif str1 == str2:
        return 1
    else:
        return 'Ни одно условие не выполнено'

print(str_comp(5, 'test'))
print(str_comp('test', 'test'))
print(str_comp('teeeest', 'test'))
print(str_comp('test', 'learn'))
print(str_comp('харумамбуру!', 'learn'))
