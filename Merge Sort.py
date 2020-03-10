def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

choosing = int(input('Choose number from 1 to 3: ' ))

'''
1 - Sort from input
2 - Sort from file
3 - Sort from list + file
'''

if choosing == 1:
    try:
        arr = list(map(int,input().split()))
    except ValueError:
        print('Bląd')

    try:
        mergeSort(arr)
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
            mergeSort(intarray)
            for i in range(len(intarray)):
                    print(intarray[i],end=' ')
        except NameError:
            print('W array istn string')

elif choosing == 3:
    try:
        arr = list(map(int,input().split()))
    except ValueError:
        print('Bląd')

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
        mergeSort(arr)
        for i in range(len(arr)):
            print(arr[i], end=' ')
    except NameError:
        print('W array istn string')
    f.close()
