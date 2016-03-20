import string
import random


def AMSestimate(vector):
    lenvect = len(vector)
    elements = dict()
    for el in vector:
        if el in elements:
            elements[el] += 1
        elif random.choice(range(0, 10)) == 0:
            elements[el] = 1
    # E(n * (2 * x.value -1))
    lendict = len(elements)
    estimateM2 = 0
    for key, value in elements.items():
        estimateM2 += lenvect * ((2 * value) - 1)
    return estimateM2/lendict


def genRandomVect(size=100):
    print(len(string.ascii_letters))
    return [random.choice(string.ascii_letters) for x in range(size)]


def secondMoment(vector):
    mydict = dict()
    for el in vector:
        if el not in mydict:
            mydict[el] = 1
        else:
            mydict[el] += 1
    return (sum([pow(value, 2) for key, value in mydict.items()]))


if __name__ == '__main__':
    vect = genRandomVect()
    print("True Second Moment:", secondMoment(vect))
    print("Estimate Second Moment with AMS:", AMSestimate(vect))
