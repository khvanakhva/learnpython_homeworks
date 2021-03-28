age = int(input('Введите ваш возраст: '))

def what_to_do(age):
    age = abs(age)
    if age < 6:
        return 'Тебе в детсад'
    elif 6 <= age <= 17:
        return 'Тебе в школу'
    elif 18 <= age <= 23:
        return 'Тебе в ВУЗ'
    else:
        return 'Пора работать'

result = what_to_do(age)

print(result)
