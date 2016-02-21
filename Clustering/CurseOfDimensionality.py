import numpy as np
from math import sqrt
from math import acos
from math import degrees
from itertools import combinations
import time

lowerbound = -1
upperbound = 1


def timer(fun):
    def wrapper(*args):
        start = time.time()
        res = fun(*args)
        end = time.time()
        print("-----------------INFO-------------------")
        print("Function {0} executed in {1:2.5} seconds".format(fun.__name__, end-start))
        print("----------------------------------------")
        return res
    return wrapper


def genRandomArray(d):
    return [np.random.uniform(lowerbound, upperbound) for i in range(0, d)]


@timer
def genSample(number, d):
    return [genRandomArray(d) for i in range(0, number)]


def euclidianDistance(point1, point2, d):
    return sqrt(sum([pow(point1[i]-point2[i], 2) for i in range(d)]))


def cosineDistance(point1, point2, d):
    num = sum([point1[i]*point2[i] for i in range(d)])
    den1 = sqrt(sum([pow(point1[i], 2) for i in range(d)]))
    den2 = sqrt(sum([pow(point2[i], 2) for i in range(d)]))
    return num / (den1 * den2)


@timer
def combinationsSample(sample):
    return list(combinations(sample, 2))


@timer
def averageDistance(distFunc, couple, d):
    lenCouple = len(couple)
    distances = [distFunc(c1, c2, d) for c1, c2 in couple]
    maxdistance = max(distances)
    mindistance = min(distances)
    return (sum(distances)/lenCouple, maxdistance, mindistance)


@timer
def standardDeviation(couple, d, average):
    lenCouple = len(couple)
    return sqrt(sum([pow(euclidianDistance(c1, c2, d) - average, 2) for c1, c2 in couple])/lenCouple)


if __name__ == '__main__':
    numsample = 100
    d = 10000
    distance = cosineDistance
    print("-----------------DATA-------------------")
    print("Uniform Distribution ({0}, {1})".format(lowerbound, upperbound))
    print("[Number of sample]: {0}".format(numsample))
    print("[Number of dimension d]: {0}".format(d))
    print("[Used distance]: {0}".format(distance.__name__))
    print("----------------------------------------")

    sample = genSample(numsample, d)
    couple = combinationsSample(sample)
    (average, maxd, mind) = averageDistance(distance, couple, d)
    stdev = standardDeviation(couple, d, average)
    print("----------------RESULTS-----------------")
    if distance.__name__ == "euclidianDistance":
        print("(lowerbound={2}) <= {0} <= (upperbound = sqrt(({2}^2)*d) = {1})".format(average, sqrt(d*pow(upperbound, 2)), pow((upperbound-lowerbound), 2)))
    print("[Standard Deviation]: ", stdev)
    print("[Max distance]: {0}".format(maxd))
    print("[Min distance]: {0}".format(mind))
    print("(MaxDistance - MinDistance)/MinDistance = {}".format((maxd-mind)/mind))
    if distance.__name__ == "cosineDistance":
        print("[Average angle]: {0}".format(degrees(acos(average))))
    print("----------------------------------------")
