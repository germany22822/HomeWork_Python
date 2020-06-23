list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
correct_list = [number for number in list if list.count(number) < 2]
print(correct_list)
