def simple_calc():
    x = float(input('выработка в часах: '))
    y = float(input('ставка в час: '))
    c = float(input('Укажите размер премии: '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')