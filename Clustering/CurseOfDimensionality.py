import numpy as np
from math import sqrt
from itertools import combinations

lowerbound = 0
upperbound = 1


def genRandomArray(d):
    return [np.random.uniform(lowerbound, upperbound) for i in range(0, d)]


def genSample(number, d):
    return [genRandomArray(d) for i in range(0, number)]


def distanceTwoPoints(point1, point2, d):
    return sqrt(sum([pow(point1[i]-point2[i], 2) for i in range(d)]))


def averageDistance(sample, d):
    couple = list(combinations(sample, 2))
    lenCouple = len(couple)
    distances = [distanceTwoPoints(c1, c2, d) for c1, c2 in couple]
    maxdistance = max(distances)
    mindistance = min(distances)
    return (sum(distances)/lenCouple, maxdistance, mindistance)


def standardDeviation(sample, d, average):
    couple = list(combinations(sample, 2))
    lenCouple = len(couple)
    return sqrt(sum([pow(distanceTwoPoints(c1, c2, d) - average, 2) for c1, c2 in couple])/lenCouple)




if __name__ == '__main__':
    numsample = 100
    d = 10000
    print("Uniform Distribution ({0}, {1})".format(lowerbound, upperbound))
    print("Number of sample: {0}".format(numsample))
    print("Number of dimension d: {0}".format(d))

    sample = genSample(numsample, d)
    (average, maxd, mind) = averageDistance(sample, d)
    print("(lowerbound={2}) <= {0} <= (upperbound = sqrt(({2}^2)*d) = {1})".format(average, sqrt(d*pow(upperbound, 2)), upperbound))
    print("Standard Deviation: ", standardDeviation(sample, d, average))
    print("Max distance: {0}".format(maxd))
    print("Min distance: {0}".format(mind))
