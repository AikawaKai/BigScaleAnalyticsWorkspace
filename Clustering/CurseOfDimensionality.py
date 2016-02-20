import numpy as np
from math import sqrt
from itertools import combinations


def genRandomArray(size):
    return [np.random.uniform(0, 1) for i in range(0, size)]


def genSample(size, d):
    return [genRandomArray(size) for i in range(0, size)]


def distanceTwoPoints(point1, point2, size):
    return sqrt(sum([pow(point1[i]-point2[i], 2) for i in range(size)]))


def averageDistance(sample, size):
    couple = list(combinations(sample, 2))
    lenCouple = len(couple)
    return sum([distanceTwoPoints(c1, c2, size) for c1, c2 in couple])/lenCouple


def standardDeviation(sample, size):
    couple = list(combinations(sample, 2))
    average = averageDistance(sample, size)
    lenCouple = len(couple)
    return sqrt(sum([pow(distanceTwoPoints(c1, c2, size) - average, 2) for c1, c2 in couple])/lenCouple)




if __name__ == '__main__':
    sample = genSample(100, 100)
    print(averageDistance(sample, 100))
    print(standardDeviation(sample, 100))
