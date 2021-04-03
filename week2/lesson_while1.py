# Задание 1
# Напишите функцию hello_user(), которая с помощью функции input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”


def hello_user():
    while True:
        user_say = input('Скажи что-нибудь: ')
        if user_say == 'Хорошо':
            break

print(hello_user())