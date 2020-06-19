all_sum = 0
i = 0
print('введите "НЕТ" если хотите закончить')
while True:
    user_num = input('введите числа через пробел:')
    input('')
    list = user_num.split()
    length = len(list)
    for sum in list:
        if sum == 'НЕТ':
            i = 1
            break
        all_sum = int(sum) + all_sum   
    print(all_sum)
    if i == 1:
        break
