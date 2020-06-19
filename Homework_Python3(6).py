user = input('введите текст: ')
def int_func(a):
    i = 0
    list = user.split()
    for itm in list:
        list[i] = itm.capitalize()
        i = i + 1
    i = 0
    txt = ''
    for itm in list:
        txt = txt + list[i] + ' '
        i = i + 1
    return txt
print(int_func(user))
