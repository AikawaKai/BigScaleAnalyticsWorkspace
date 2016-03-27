import matplotlib.pyplot as plt
from numpy import random
from itertools import combinations
from math import sqrt

'''
plt.plot([1, 2, 3, 4], [2, 3, 4, 5], 'ro')
plt.axis([0, 20, 0, 20])
plt.ylabel('some numbers')
plt.show()'''


class Cluster(object):

    def __init__(self, point):
        self.listOfPoint = []
        self.len = 1
        self.listOfPoint.append(point)
        self.centroid = point
        self.sum1 = point[0]
        self.sum2 = point[1]

    def addPoint(self, point):
        self.listOfPoint.append(point)
        self.len += 1
        self.sum1 += point[0]
        self.sum2 += point[1]
        self.computeCentroid()

    def computeCentroid(self):
        self.centroid = [self.sum1/self.len, self.sum2/self.len]

    def euclideanDist(self, other):
        x = self.centroid
        y = other.centroid
        return sqrt(sum([pow(x[i]-y[i], 2) for i in range(self.len)]))


def genSample(size):
    return [random.random_integers(0, 100, 2) for x in range(size)]


if __name__ == '__main__':
    listOfPoint = genSample(100)
    # print(listOfPoint)
    list1 = []
    list2 = []
    for ele in listOfPoint:
        list1.append(ele[0])
        list2.append(ele[1])
    # print(list1, list2)
    plt.plot(list1, list2, 'wo')
    plt.axis([0, 100, 0, 100])
    plt.ylabel('some numbers')
    # plt.show()
    listOfCluster = [Cluster(point) for point in listOfPoint]
    combList = combinations(listOfCluster, 2)
    for x, y in combList:
        print(x.euclideanDist(y))
