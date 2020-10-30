# Copyright (c)2020 BugMaker-Project
# A Script for sorting.
from numpy.random import randint
def InsertSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr
def SelectSort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr
def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def QuickSort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return QuickSort(less) + [pivot] + QuickSort(greater)
def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
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
def ShellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            current = arr[i]
            while j - gap >= 0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        gap //= 2
    return arr
def RadixSort(arr,d):
    for k in range(d):
        s=[[] for i in range(10)]
        for i in arr:
            s[i//(10**k)%10].append(i)
        arr=[j for i in s for j in i]
    return arr
def ConutingSort(A):
    k = max(A)
    C = [0]*(k+1)
    B = (len(A))*[0]
    for i in range(0, len(A)):
        C[A[i]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
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