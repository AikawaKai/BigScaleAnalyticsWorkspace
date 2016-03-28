import matplotlib.pyplot as plt
from numpy import random as randomN
from itertools import combinations
from itertools import product
from math import sqrt
import random


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def euclideanDist(self, other):
        return sqrt(sum([pow(self.x-other.x, 2), pow(self.y-other.y, 2)]))


class Cluster(object):

    def __init__(self, point):
        self.listOfPoint = []
        self.len = 1
        self.listOfPoint.append(point)
        self.centroid = point
        self.sum1 = point.x
        self.sum2 = point.y
        self.ray = 0

    def addPoint(self, point):
        self.listOfPoint.append(point)
        self.len += 1
        self.sum1 += point.x
        self.sum2 += point.y
        self.computeCentroid()
        self.ray = 0
        for point in self.listOfPoint:
            self.ray += self.euclideanDistPoint(point)
        self.ray = self.ray/self.len

    def computeCentroid(self):
        self.centroid = Point(self.sum1/self.len, self.sum2/self.len)

    def euclideanDist(self, other):
        c1 = self.centroid
        c2 = other.centroid
        return sqrt(sum([pow(c1.x-c2.x, 2), pow(c1.y-c2.y, 2)]))

    def euclideanDistPoint(self, point):
        c1 = self.centroid
        c2 = point
        return sqrt(sum([pow(c1.x-c2.x, 2), pow(c1.y-c2.y, 2)]))


def genSample(size):
    return [randomN.random_integers(0, 100, 2) for x in range(size)]


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
            list1.append(point.x)
            list2.append(point.y)
        plt.plot(list1, list2, 'o'+setcolor[i])
        plt.plot([cluster.centroid.x], [cluster.centroid.y], 'xk')
        i += 1
        if i > 7:
            i = 0

powers2 = [pow(2, i) for i in range(1, 10)]


def meanrayClusters(setClusters):
    sumray = 0
    for cluster in setClusters:
        sumray += cluster.ray
    return sumray/len(setClusters)


def addPointsToSet(k_points, setPoint, numToAdd):
    listpoints = [random.sample(setPoint, numToAdd) for i in range(10)]
    couple_dist = []
    for points in listpoints:
        prod = product(k_points, points)
        temp_distance = (sum([x.euclideanDist(y) for x, y in prod]), points)
        couple_dist.append(temp_distance)
    max_dist = max(couple_dist, key=lambda x: x[0])
    points = max_dist[1]
    for point in points:
        k_points.add(point)
    for point in points:
        setPoint.remove(point)


def k_means(points):
    setPoint = set(points)
    first = random.sample(setPoint, 1)[0]
    k_points = set()
    k_points.add(first)
    setPoint.remove(first)
    setClusters = {Cluster(point) for point in k_points}
    k_means_core(setPoint, setClusters)
    meanray = meanrayClusters(setClusters)
    diff = 10
    for pow2 in powers2:
        if pow2 > len(setPoint):
            break
        addPointsToSet(k_points, setPoint, pow2 - len(k_points))
        setClusters = {Cluster(point) for point in k_points}
        k_means_core(setPoint, setClusters)
        currmeanray = meanrayClusters(setClusters)
        if(abs(abs(currmeanray-meanray)-diff) < 0.8):
            break
        meanray = currmeanray
    return setClusters


def k_means_core(setPoint, setClusters):
    for point in setPoint:
        distances = [(cluster.euclideanDistPoint(point), cluster)
                     for cluster in setClusters]
        mindist = min(distances, key=lambda x: x[0])
        selectedcluster = mindist[1]
        selectedcluster.addPoint(point)

if __name__ == '__main__':
    listOfPoint = genSample(100)
    listOfPoint = [Point(p[0], p[1]) for p in listOfPoint]
    # print(listOfPoint)
    list1 = []
    list2 = []
    plt.figure(0)
    plt.axis([0, 100, 0, 100])
    listOfCluster = [Cluster(point) for point in listOfPoint]
    setClusters = hierarchyClustering(listOfCluster, 7)
    plotClusters(setClusters)
    plt.figure(1)
    setClusters = k_means(listOfPoint)
    print(len(setClusters))
    plotClusters(setClusters)
    plt.show()
