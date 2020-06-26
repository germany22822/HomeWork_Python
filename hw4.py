re_name_1 = ['Один', 'Два', 'Три'  ,'Четыре']
re_name_2 = ['One' , 'Two', 'Three',  'Four']
int_my = 0
file = open('test_4.txt', 'r')
for i in file.readlines():
    print(i)
    i.replace(re_name_2[int_my], re_name_1[int_my])
    int_my += 1
