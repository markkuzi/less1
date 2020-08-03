class Matrix:
    matr = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    def __init__(self, matr_1, matr_2):
        self.matr_1 = matr_1
        self.matr_2 = matr_2

    def __add__(self):

        for i in range(len(self.matr_1)):

            for j in range(len(self.matr_2[i])):
                self.matr[i][j] = self.matr_1[i][j] + self.matr_2[i][j]

        return self.matr

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.__add__()]))


my_matr = Matrix([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 [[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]])

print(my_matr.__str__())
