# Задание
# Создайте список из чисел 3, 5, 7, 9 и 10.5
# Выведите содержимое списка на экран
# Добавьте в конец списка строку "Python"
# Выведите длину списка на экран
# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"



num_list = [3, 5, 7, 9, 10.5]

print(num_list)

num_list.append('Python')
print(num_list)

print(len(num_list))

print(num_list[0])

print(num_list[-1])

print(num_list[2:5])

num_list.remove('Python')

print(num_list)