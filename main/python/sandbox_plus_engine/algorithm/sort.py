# Copyright (c)2020 BugMaker-Project
# array Script for sorting.
from numpy.random import randint
def InsertSort(array):
    for i in range(1, len(array)):
        current = array[i]
        pre_index = i - 1
        while pre_index >= 0 and array[pre_index] > current:
            array[pre_index + 1] = array[pre_index]
            pre_index -= 1
        array[pre_index + 1] = current
    return array
def SelectSort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array
def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def QuickSort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return QuickSort(less) + [pivot] + QuickSort(greater)
def MergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return __marge(MergeSort(left), MergeSort(right))
def __marge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
def ShellSort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            j = i
            current = array[i]
            while j - gap >= 0 and current < array[j - gap]:
                array[j] = array[j - gap]
                j -= gap
            array[j] = current
        gap //= 2
    return array
def RadixSort(array,d):
    for k in range(d):
        s=[[] for i in range(10)]
        for i in array:
            s[i//(10**k)%10].append(i)
        array=[j for i in s for j in i]
    return array
def ConutingSort(array):
    k = max(array)
    C = [0]*(k+1)
    B = (len(array))*[0]
    for i in range(0, len(array)):
        C[array[i]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(len(array)-1, -1, -1):
        B[C[array[i]]-1] = array[i]
        C[array[i]] -= 1
    return B
#桶排序
def bucket_sort(the_list):
    #设置全为0的数组
    all_list = [0 for i in range(100)]
    last_list = []
    for v in the_list:
        all_list[v] = 1 if all_list[v]==0 else all_list[v]+1
    for i,t_v in enumerate(all_list):
        if t_v != 0:
            for j in range(t_v):
                last_list.append(i)
    return last_list