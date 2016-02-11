
def counter(fun):
    fun.count = 0

    def wrapper(*args):
        fun.count += 1
        res = fun(*args)
        return res
    return wrapper


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

    def __mul__(self, elem):
        if type(elem) is float:
            vectresult = list(map(lambda x: x * elem, self.vector))
            return Vector(vectresult)

    def cleanVector(self):
        self.vector = list(map(lambda x: x if x > 0.0009 else 0, self.vector))

    def generateVector1n(n):
        return Vector([1/n for i in range(0, n)])

    def generateMaskVector(maskvector):
        s = sum(maskvector)
        return Vector(list(map(lambda x: 1/s if x == 1 else 0, maskvector)))

    def __str__(self, precision=7):
        basic = ""
        for elem in self.vector:
            el = "{0:>10.{1}} ".format(float(elem), precision)
            basic += el
        return basic


class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])

    def mulVect(self, vector):
        resV = []
        for row in self.matrix:
            elem = vector.mulSum(Vector(row))
            resV.append(elem)
        return Vector(resV)

    def transpose(self):
        tran = [[self.matrix[i][j] for i in range(self.row)] for j in range(self.column)]
        return Matrix(tran)

    def __str__(self):
        basic = ""
        for row in self.matrix:
            for elem in row:
                basic += "{0:>4.2} ".format(float(elem))
            basic += "\n"
        return basic


# v' = M * v  without spider traps or dead ends
def basicPageRank(matrix, v, pv):
    diffv = v - pv
    # print("Current:{0} Previous:{1}".format(v, pv))
    # print("Diff {0}".format(diffv), end="\n\n")
    return v if sum(diffv.vector) <= 0.0009 else basicPageRank(matrix, matrix.mulVect(v),v)


#  Beta * M * v + (1 - Beta) * 1/n * 1v taxation for spider traps and dead ends
def taxationPageRank(matrix, v, pv, vn):
    diffv = v - pv
    # print("Current:{0} Previous:{1}".format(v, pv))
    # print("Diff {0}".format(diffv), end="\n\n")
    return v if sum(diffv.vector) <= 0.0009 else taxationPageRank(matrix, (matrix.mulVect(v) * 0.8) + (vn * 0.2), v, vn)


def trustRank(matrix, v, pv, vnmask):
    diffv = v - pv
    # print("Current:{0} Previous:{1}".format(v, pv))
    # print("Diff {0}".format(diffv), end="\n\n")
    return v if sum(diffv.vector) <= 0.0009 else trustRank(matrix, (matrix.mulVect(v) * 0.8) + (vnmask * 0.2), v, vnmask)


def normalize(vect, max):
    v = vect.vector
    return Vector(list(map(lambda x: x/max, v)))


def hubbinessAuthority(L, Lt, ph, pa):
    a = Lt.mulVect(ph)
    h = L.mulVect(a)
    maxa = max(a.vector)
    maxh = max(h.vector)
    a = normalize(a, maxa)
    h = normalize(h, maxh)
    diffa = a - pa
    diffh = h - ph
    return (a, h) if sum(diffa.vector) <= 0.0009 and sum(diffh.vector) <= 0.0009 else hubbinessAuthority(L, Lt, h, a)



if __name__ == '__main__':
    matrix = [[1/3, 0, 1/2, 0], [1/3, 1/2, 0, 1/3], [1/3, 1/2, 0, 1/3],
              [0, 0, 1/2, 1/3]]
    basicVector = Vector([1/4, 1/4, 1/4, 1/4])
    Matrix1 = Matrix(matrix)
    vectorResult = basicPageRank(Matrix1, basicVector, Vector([1, 1, 1, 1]))
    print("\n#Basic example with a connected graph\n")
    print("Matrix:\n")
    print(Matrix1)
    print("Page Rank basic: {0}".format(str(vectorResult)))

    matrix1 = [[0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2],
               [1/3, 1/2, 0, 0]]
    Matrix2 = Matrix(matrix1)
    print("_____________________________________________________", end="\n\n")
    print("#Another example with a connected graph\n")
    print("Matrix:\n")
    print(Matrix2)
    vectorResultPageRank = basicPageRank(Matrix2, basicVector, Vector([1, 1, 1, 1]))
    print("Page Rank basic: {0}".format(str(vectorResultPageRank)), end="\n\n")

    matrix3 = [[0, 1/2, 0, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2],
               [1/3, 1/2, 0, 0]]
    Matrix4 = Matrix(matrix3)
    print("_____________________________________________________", end="\n\n")
    print("#Another example with a graph with a dead end\n")
    print("Matrix:\n")
    print(Matrix4)
    vectorResult = basicPageRank(Matrix4, basicVector, Vector([1, 1, 1, 1]))
    print("Page Rank basic: {0}".format(str(vectorResult)), end="\n\n")

    vn = Vector.generateVector1n(4)
    matrix2 = [[0, 1/2, 0, 0], [1/3, 0, 0, 1/2], [1/3, 0, 1, 1/2],
               [1/3, 1/2, 0, 0]]
    Matrix3 = Matrix(matrix2)
    vectorResult = basicPageRank(Matrix3, basicVector, Vector([1, 1, 1, 1]))
    print("_____________________________________________________", end="\n\n")
    print("#Without taxation all the probability goes to the third vertex")
    print("Matrix:\n")
    print(Matrix3)
    print("Page Rank basic: {0}".format(str(vectorResult)), end="\n\n")

    print("_____________________________________________________", end="\n\n")
    vectorResult = taxationPageRank(Matrix3, basicVector, Vector([1, 1, 1, 1]), vn)
    print("#Same Matrix: With the taxation we provide a better pagerank value (Beta=0.8)")
    print("Matrix:\n")
    print(Matrix3)
    print("Page Rank taxation: {0}".format(str(vectorResult)))

    print("_____________________________________________________", end="\n\n")
    print("TrustRank: Node 1 e 3 trusted. Beta=0.8 ")
    print("Matrix:\n")
    print(Matrix2)
    maskvector = Vector.generateMaskVector([0, 1, 0, 1])
    print(maskvector)
    vectorResultTrust = trustRank(Matrix2, basicVector, Vector([1, 1, 1, 1]), maskvector)
    print("Trust Rank (node 1 and 3): {0}".format(str(vectorResultTrust)))

    print("_____________________________________________________", end="\n\n")
    print("Spam Mass checking", end="\n\n")
    print("{:>7} {:>10} {:>10} {:>10}".format("Nodo", "PageRank", "TrustRank", "SpamMass"))
    pagerank = vectorResultPageRank.vector
    trustrank = vectorResultTrust.vector
    for i in range(len(pagerank)):
        t = trustrank[i]
        r = pagerank[i]
        print("{:>7} {:>10.3} {:>10.3} {:>10.3}".format(i, r, t, (r-t)/r))

    print("\n\n_____________________________________________________", end="\n\n")
    L = [[0, 1, 1, 1, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0]]
    MatrixL = Matrix(L)
    print("")
    print(MatrixL)
    MatrixLt = MatrixL.transpose()
    print(MatrixLt)
    (a, h) = hubbinessAuthority(MatrixL, MatrixLt, Vector([1, 1, 1, 1, 1]),
                                Vector([1, 1, 1, 1, 1]))
    a.cleanVector()
    h.cleanVector()
    print("\nHubbiness:")
    print(h.__str__(3))

    print("\nAuthority:")
    print(a.__str__(3))
