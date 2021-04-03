# Оценки
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '6a', 'scores': [4, 5, 5, 3, 3]},
    {'school_class': '5a', 'scores': [3, 3, 3, 3, 3]}
]

points = 0
students = 0

for klass in school_scores:
    print(f'Средний бал в классе {klass["school_class"]} составляет {sum(klass["scores"]) / len(klass["scores"])}')
    points += sum(klass["scores"])
    students += len(klass["scores"])

print(f'Средний бал в школе составляет {points/students}')


