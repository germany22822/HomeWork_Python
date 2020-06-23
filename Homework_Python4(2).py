print('введите числа через пробел')
my_list = [int(i) for i in input().split()]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        print(my_list[i]) 
