import numpy as np
from time import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# print quicksort([3,6,8,10,1,2,1])
# Prints "[1, 1, 2, 3, 6, 8, 10]"

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    # pivot = np.array(arr).mean()/2
    pivot = max(arr)
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x> pivot]
    middle = [x for x in arr if x==pivot]
    return quick_sort(left)+middle+quicksort(right)

def qSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = [lst[len(lst)/2]]
    left = [x for x in lst if x < pivot[0]]
    right = [x for x in lst if x > pivot[0]]
    return qSort(left) + pivot + qSort(right)

print quick_sort([12,6,3,8,10,1,34,2,12,23,2,5,34,32,1])
print quick_sort([0,1,1,0,1,1,0,0])
print qSort([12,6,3,8,10,1,34,2,12,23,2,5,34,32,1])

# print quick_sort(np.array([6,3,8,10,1,2,1]))