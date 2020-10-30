# Copyright (c)2020 BugMaker-Project
# A Script for Searching.
def SequentialSearch(array, key):
  length = len(array)
  for i in range(length):
    if array[i] == key:
      return i
    else:
      return False
def BinarySearch(array, key):
  low = 0
  high = len(array) - 1
  while low < high:
    mid = int((low + high) / 2)
    if key < array[mid]:
      high = mid - 1
    elif key > array[mid]:
      low = mid + 1
    else:
      return mid
  return False
def InterpolationSearch(array, key):
  low = 0
  high = len(array) - 1
  while low < high:
    mid = low + int((high - low) * (key - array[low])/(array[high] - array[low]))
    if key < array[mid]:
      high = mid - 1
    elif key > array[mid]:
      low = mid + 1
    else:
      return mid
  return False
def fibonacci_search(array, key):
  F = [
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
     233, 377, 610, 987, 1597, 2584, 4181, 6765,
     10946, 17711, 28657, 46368
     ]
  low = 0
  high = len(array) - 1
  k = 0
  while high > F[k]-1:
    k += 1
  i = high
  while F[k]-1 > i:
    array.append(array[high])
    i += 1
  while low <= high:
    if k < 2:
      mid = low
    else:
      mid = low + F[k-1]-1
    if key < array[mid]:
      high = mid - 1
      k -= 1
    elif key > array[mid]:
      low = mid + 1
      k -= 2
    else:
      if mid <= high:
        return mid
      else:
        return high
  return False