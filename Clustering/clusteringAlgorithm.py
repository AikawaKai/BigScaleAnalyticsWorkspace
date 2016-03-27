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
        return sqrt(sum([pow(x[i]-y[i], 2) for i in range(2)]))


def genSample(size):
    return [random.random_integers(0, 100, 2) for x in range(size)]


def hierarchyClustering(clusters, numclusters):
    setClusters = set(clusters)
    numtot = len(setClusters)
    if(numtot <= numclusters):
        return clusters
    while numtot > numclusters:
        combList = combinations(setClusters, 2)
        listDistance = []
        for x, y in combList:
            listDistance.append((x.euclideanDist(y), (x, y)))
        coupleMinDistance = min(listDistance, key=lambda x: x[0])
        for point in coupleMinDistance[1][1].listOfPoint:
            coupleMinDistance[1][0].addPoint(point)
        setClusters.remove(coupleMinDistance[1][1])
        numtot = len(setClusters)
    return setClusters


setcolor = ['b', 'r', 'g', 'y', 'm', 'k', 'w', 'c']


def plotClusters(setClusters):
    plt.axis([0, 100, 0, 100])
    i = 0
    for cluster in setClusters:
        l = cluster.listOfPoint
        list1 = []
        list2 = []
        for point in l:
            list1.append(point[0])
            list2.append(point[1])
        plt.plot(list1, list2, 'o'+setcolor[i])
        i += 1
    plt.show()





if __name__ == '__main__':
    listOfPoint = genSample(100)
    # print(listOfPoint)
    list1 = []
    list2 = []
    for ele in listOfPoint:
        list1.append(ele[0])
        list2.append(ele[1])
    # print(list1, list2)
    # plt.plot(list1, list2, 'wo')
    plt.axis([0, 100, 0, 100])
    # plt.ylabel('some numbers')
    # plt.show()
    listOfCluster = [Cluster(point) for point in listOfPoint]
    setClusters = hierarchyClustering(listOfCluster, 8)
    plotClusters(setClusters)
