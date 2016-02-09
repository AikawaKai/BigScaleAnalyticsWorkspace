class Vector(object):

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        vector = []
        for i in range(len(self.vector)):
            elem = abs(self.vector[i]+other.vector[i])
            vector.append(elem)
        return Vector(vector)

    def __sub__(self, other):
        vector = []
        for i in range(len(self.vector)):
            elem = abs(self.vector[i]-other.vector[i])
            vector.append(elem)
        return Vector(vector)

    def mulSum(self, other):
        vector = []
        for i in range(len(self.vector)):
            elem = self.vector[i]*other.vector[i]
            vector.append(elem)
        return sum(vector)

    def __str__(self):
        basic = ""
        for elem in self.vector:
            el = "{0:>10.7} ".format(float(elem))
            basic += el
        return basic


class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def mulVect(self, vector):
        resV = []
        for row in self.matrix:
            elem = vector.mulSum(Vector(row))
            resV.append(elem)
        return Vector(resV)


def basicPageRank(matrix, v, pv):
    diffv = v - pv
    print("Current:{0} Previous:{1}".format(v, pv))
    print("Diff {0}".format(diffv), end="\n\n")
    return v if sum(diffv.vector) <= 0.0009 else basicPageRank(matrix, matrix.mulVect(v),v)


if __name__ == '__main__':
    matrix = [[1/3, 0, 1/2, 0], [1/3, 1/2, 0, 1/3], [1/3, 1/2, 0, 1/3],
              [0, 0, 1/2, 1/3]]
    basicVector = Vector([1/4, 1/4, 1/4, 1/4])
    Matrix1 = Matrix(matrix)
    vectorResult = basicPageRank(Matrix1, basicVector, Vector([1, 1, 1, 1]))
    print("Page Rank: {0}".format(str(vectorResult)))
    matrix1 = [[0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2],
               [1/3, 1/2, 0, 0]]
    Matrix2 = Matrix(matrix1)
    vectorResult = basicPageRank(Matrix2, basicVector, Vector([1, 1, 1, 1]))
    print("Page Rank: {0}".format(str(vectorResult)))
