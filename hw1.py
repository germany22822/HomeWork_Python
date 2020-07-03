class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    def __add__(self):
        mat = [[],
               [],
               []]
        self.mat = mat
        for i in range(len(self.list_1)):
            for l in range(len(self.list_2[i])):
                mat[i].append(self.list_1[i][l] + self.list_2[i][l])
    def __str__(self):
        a = 0
        b = 0
        return print(f'{self.mat[a][b]} {self.mat[a][b + 1]} \n{self.mat[a + 1][b]} {self.mat[a][b + 1]} \n{self.mat[a + 2][b]} {self.mat[a][b + 1]}')
m = Matrix([[44, 35],
            [8, 100],
            [4, 55]],
           [[14, 10],
            [8, 200],
            [1, 7]])
print(m.__add__())
print(m.__str__())
