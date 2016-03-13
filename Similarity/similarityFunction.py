def jaccardSimilarity(set1, set2):
    inter = set.intersection(set1, set2)
    union = set.union(set1, set2)
    print(inter, union)
    return (len(inter)/len(union))

if __name__ == '__main__':
    set1 = {1, 2, 3, 5, 7, 10}
    set2 = {2, 3, 7, 10, 11}
    print(jaccardSimilarity(set1, set2))
