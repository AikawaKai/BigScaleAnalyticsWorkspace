import numpy as np
from math import sqrt
from itertools import combinations


def genRandomArray(d):
    return [np.random.uniform(0, 1) for i in range(0, d)]


def genSample(number, d):
    return [genRandomArray(d) for i in range(0, number)]


def distanceTwoPoints(point1, point2, d):
    return sqrt(sum([pow(point1[i]-point2[i], 2) for i in range(d)]))


def averageDistance(sample, d):
    couple = list(combinations(sample, 2))
    lenCouple = len(couple)
    return sum([distanceTwoPoints(c1, c2, d) for c1, c2 in couple])/lenCouple


def standardDeviation(sample, d):
    couple = list(combinations(sample, 2))
    average = averageDistance(sample, d)
    lenCouple = len(couple)
    return sqrt(sum([pow(distanceTwoPoints(c1, c2, d) - average, 2) for c1, c2 in couple])/lenCouple)




if __name__ == '__main__':
    numsample = 100
    d = 1000
    sample = genSample(numsample, d)
    average = averageDistance(sample, d)
    print("(lowerbound = 1) <= {0} <= (upperbound = sqrt(d) = {1})".format(average, sqrt(d)))
    print("Standard Deviation: ", standardDeviation(sample, d))
