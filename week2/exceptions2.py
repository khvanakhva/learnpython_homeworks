# Задание 2
# Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
# чтобы она перехватывала исключения, когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, если приведение типов не сработало.

# def discounted_price(price, discount):
#     try:
#         price = abs(float(price))
#         discount = abs(float(price))
#     except ValueError:
#         print('Вы ввели некорректные данные.')
#     if discount >= 100:
#         price_with_dicount = price
#     else:
#         price_with_dicount = price - (price * discount / 100)
#     return price_with_dicount

# print(discounted_price(150, 15))
# print(discounted_price('hello', 15))


def discounted(price, discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
    except ValueError:
        return print('Введены некорректные данные.')
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)


discounted(100, 80)
discounted('hello', 45)
