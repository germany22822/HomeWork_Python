n_1 = int(input('введите первое число: '))
n_2 = int(input('введите второе число: '))
n_3 = int(input('введите третье число: '))
def my_func(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    a = list.index(min(list))
    list.remove(a)
    return sum(list)
print(my_func(n_1, n_2, n_3))
    
    