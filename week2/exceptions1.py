# Задание 1
# Перепишите функцию hello_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи оператора breaк


def hello_user():
    while True:
        try:
            user_say = input('Скажи что-нибудь: ')
            if user_say == 'Хорошо':
                break
        except KeyboardInterrupt:
            print('Пока')
            break

hello_user()