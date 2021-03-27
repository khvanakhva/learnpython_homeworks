# Задание 1
# Создайте функцию get_summ(one, two, delimiter='&'), 
# которая принимает два параметра, приводит их к строке 
# и отдает объединенными через разделитель delimiter
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
# положите результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами



def get_summ(one, two, delimiter=' & '):
    one = str(one)
    two = str(two)

    return one + delimiter + two

result = get_summ('Learn', 'python').upper()
print(result)