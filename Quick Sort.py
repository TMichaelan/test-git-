import time
start_time = time.time()

"""
Функция берет последний элемент как пивот ,
ставит его в нужное место в массиве,
все числа, которые меньше чем пивот ставит в лево,
а те которые больше его ставит в право пивота.
Только в моем случае наоборот, потому что я делаю
сортировку от большего к меньшему
"""


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] >= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i]),


try:
    print("1 - Sort from input")
    print("2 - Sort from file")
    print("3 - Sort from list + file")
    choosing = int(input('Choose number from 1 to 3: ' ))
except ValueError:
    choosing = 0


'''
1 - Sort from input
2 - Sort from file
3 - Sort from list + file
'''
if choosing > 3:
    print('You must enter from 1 to 3!')
if choosing == 0:
    print('You must enter from 1 to 3!')

if choosing == 1:
    try:
        arr = list(map(int,input().split()))
        n = len(arr)
    except ValueError:
        print('Bląd')

    try:
        quickSort(arr, 0, n - 1)
        for i in range(len(arr)):
            print(arr[i], end=' ')
    except NameError:
        print('W array istn string')

elif choosing == 2:
    for i in range(1):
        try:
            f = open('main.txt', 'r')
            line = f.readline()
            array = []
            array.append(line.split())
            for minusskoby in array:
                pass
            intarray = []
            for i in minusskoby:
                x = int(i)
                intarray.append(x)
        except ValueError:
            print('Blęd Value Error')
            break

        try:
            n = len(intarray)
            quickSort(intarray, 0, n - 1)
            for i in range(len(intarray)):
                    print(intarray[i],end=' ')
        except NameError:
            print('W array istn string')

elif choosing == 3:
    flag = 0
    try:
        arr = list(map(int,input().split()))
        n = len(arr)
    except ValueError:
        flag = 1
    if flag == 1:
        print("Bląd")
    else:
        try:
            f = open('main.txt', 'r')
            line = f.readline()
            array = []
            array.append(line.split())
            for minusskoby in array:
                pass
            intarray = []
            for i in minusskoby:
                x = int(i)
                intarray.append(x)
            for i in intarray:
                arr.append(i)
        except ValueError:
            print('Blęd Value Error')

        try:
            n = len(arr)
            quickSort(arr, 0, n - 1)
            for i in range(len(arr)):
                print(arr[i], end=' ')
        except NameError:
            print('W array istn string')
        f.close()
print()
print("Time: %s seconds " % (time.time() - start_time))