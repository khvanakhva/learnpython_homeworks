# Задание

# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь
# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словар


my_dict = {
    'city': 'Москва',
    'temperature': '20',
}

print(my_dict['city'])

my_dict['temperature'] = '15'

print(my_dict)

print(my_dict.get('country', 'Россия'))

my_dict['date'] = '27.05.2019'
print(my_dict)

print(len(my_dict))
