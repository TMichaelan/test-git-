def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


try:
    arr = list(map(int,input().split()))
# arr = [13, 11, 13, 5, 6]
except ValueError:
    print('Bląd')
try:
    insertionSort(arr)
    for i in range(len(arr)):
            print(arr[i],end=' ')
except NameError:
    print('W array istn string')
