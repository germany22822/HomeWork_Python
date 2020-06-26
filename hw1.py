file = open('test.txt', 'w')
while True:
    user = input('Введите текст: ')
    file.writelines(user)
    if user == '':
        break

file.close()
file = open('test.txt', 'r')
print(file.readlines())
file.close()
