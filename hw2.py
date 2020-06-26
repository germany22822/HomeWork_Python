my_max = 0
file = open('test_2.txt', 'r')
print(f'Содержимое файла: \n{file.read()}')
file = open('test_2.txt', 'r')
print(f'Количество строк в файле - {len(file.readlines())}\n')
file = open('test_2.txt', 'r')
for i in file.readlines():
    file = open('test_2.txt', 'r')
    num = len(i) - 1
    my_max += num
    print(f'{str(num)} слов в строке - {i}')
print(f'Общее количество слов - {my_max}')
file.close() 
