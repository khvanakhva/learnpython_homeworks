# def discounted(price, discount, max_discount=50):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     max_discount = abs(float(max_discount))
#     if max_discount > 99:
#         raise ValueError('Max discount can`t be more than 99%')
#     if discount >= max_discount:
#         price_with_discount = price
#     else:
#         price_with_discount = price - price * discount / 100
#     return price_with_discount


# print(discounted(100, 40))


def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

result = format_price(56.24)
print(result)

