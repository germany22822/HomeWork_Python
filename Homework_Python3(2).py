name = input('имя: ')
last_name = input('фамилия: ')
age = input('возраст: ')
city = input('город проживания: ')
mail = input('почта: ')
phone = input('телефон: ')
def user(a, b, c, d, e, f):
    end = f'({a}) имя, ({b}) фамилия, ({c}) возраст, ({d}) город, ({e}) почта, ({f}) телефон, данные о {a}'
    return end
print(user(name, last_name, age, city, mail, phone))
