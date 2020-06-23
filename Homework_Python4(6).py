from itertools import cycle
from itertools import count
i = 0

user = int(input('введите кол-во раз: '))
new_list = ['Имя', 444, False]
for obj in cycle(new_list):
    i += 1
    print(obj)
    if i == user * 3:
        break

user_first = input('Введите стартовое число: ')
user_end = int(input('Введите конечное число: '))
for obj in count(int(user_first)):
    if obj == user_end + 1:
        break
    print(obj)
