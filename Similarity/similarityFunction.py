def jaccardSimilarity(set1, set2):
    inter = set.intersection(set1, set2)
    union = set.union(set1, set2)
    return (len(inter)/len(union))


def returnDict(list1):
    dict1 = dict()
    for el in list1:
        if el not in dict1:
            dict1[el] = 1
        else:
            dict1[el] += 1
    return dict1


def jaccardSimilarityWithMultiSet(list1, list2):
    dict1 = returnDict(list1)
    dict2 = returnDict(list2)
    inter = sum([min(value, dict2[key]) for key, value in dict1.items() if key in dict2])
    union = len(list1)+len(list2)
    return (inter/union)

if __name__ == '__main__':
    set1 = {1, 2, 3, 5, 7, 10}
    set2 = {2, 3, 7, 10, 11}
    print(jaccardSimilarity(set1, set2))
    list1 = ['a', 'a', 'a', 'b']
    list2 = ['a', 'a', 'b', 'b', 'c']
    print(jaccardSimilarityWithMultiSet(list1, list2))
