import random


def createArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 100))
    print("original array" + str(array))
    return array

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print("sorting array" + str(array))
    print("sorted array" + str(array))


def mergeSort(size):
    l = 0
    r = len(array) - 1
    m = (l + r) // 2
    n1 = m-l+1
    n2 = r-m
    leftArr = [0] * n1
    rightArr = [0] * n2
    for i in range(n1):
        leftArr[i] = array[l + i]
    for j in range(n2):
        rightArr[j] = array[m + 1 + j]
    i, j, k = 0, 0, l
    #unfinished


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        print("sorting array" + str(array))
    print("sorted array" + str(array))








size = 10
array = createArray(size)
x = array
y = array
print("x" + str(x))
print("y" + str(y))
insertionSort(x)
print("x" + str(x))
print("y" + str(y))
bubbleSort(y)
