a = int(input('введите 1 число: '))
b = int(input('введите 2 число: '))
def my_function(num_1, num_2):
    if num_2 == 0:
        error = 'на 0 делить нельзя'
        return error
    end = num_1 / num_2
    return end
print(my_function(a, b))
