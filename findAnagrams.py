from time import time
import timeit
from collections import Counter, defaultdict
from itertools import permutations

def find_anagrams1(lst):
    result = []
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i+1:]):
            if sorted(word1) == sorted(word2) and word1 not in result:
                result.append(word1)
            if sorted(word1) == sorted(word2) and word2 not in result:
                result.append(word2)
                break
    return result

def find_anagrams2(lst):
    result = []
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i+1:]):
            if sorted(word1) == sorted(word2):
                result.append(word1)
                result.append(word2)
                break
    return list(set(result))

def find_anagrams_permu(lst):
    results = []
    for word1 in lst:
        for word2 in lst:
            if word1 != word2:
                for perm in permutations(word1):
                    if perm == tuple(word2) and word1 not in results:
                        results.append(word1)
    return results

def find_anagrams_notin(lst):
    results = []
    for word1 in lst:
        for word2 in lst:
            if word1!=word2 and sorted(word1)==sorted(word2) and word1 not in results:
                results.append(word1)
    return results

def find_anagrams_sortbrk(lst):
    results = []
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 and sorted(word1) == sorted(word2):
                results.append(word1)
                break
    return results

def find_anagrams_counter(lst):
    results = []
    for word1 in lst:
        for word2 in lst:
            if word1!=word2 and Counter(word1)==Counter(word2):
                results.append(word1)
                break
    return results

def find_anagrams_dct(lst):
    dct = defaultdict(list)
    result = []
    for word in lst:
        dct[tuple(sorted(word))].append(word)
    for key, value in dct.iteritems():
        if len(value)>1:
            result.extend(value)
    return result

def cal_time(func, lst):
    start = time()
    func(lst)
    end = time()
    period = (end-start)*1000
    print 'For time, %s run time is: %f ms.' %(func.__name__, period)
    start_time = timeit.default_timer()
    func(lst)
    print 'For timeit, %s run time is: %f ms.' %(func.__name__, (timeit.default_timer() - start_time)*1000)
    print func(lst)

def findit1(lst): #diversity to highly ordered
    d = {}
    result = []
    for word in lst: #setup data structure, find by conition using available resourses such as index, zip/tuple pairs
        if tuple(sorted(word)) not in d:
            d[tuple(sorted(word))] = []
        d[tuple(sorted(word))].append(word)
    for key, value in d.iteritems():
        if len(value) > 1:
            result.extend(value)
    return result

def findit(lst):
    d = defaultdict(list)
    result = []
    for word in lst:
        d[tuple(sorted(word))].append(word)
    for key, value in d.iteritems():
        if len(value) > 1:
            result.extend(value)
    return result

if __name__=='__main__':
    lst = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star']
    cal_time(find_anagrams_counter,lst)
    cal_time(find_anagrams_permu,lst)
    cal_time(find_anagrams_notin, lst)
    cal_time(find_anagrams_sortbrk,lst)
    cal_time(find_anagrams_dct,lst)
    cal_time(find_anagrams1, lst)
    cal_time(find_anagrams2, lst)
    print findit(lst)
    print findit1(lst)