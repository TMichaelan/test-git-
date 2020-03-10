def ShellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


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
        ShellSort(arr)
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
            ShellSort(intarray)
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
        ShellSort(arr)
        for i in range(len(arr)):
            print(arr[i], end=' ')
    except NameError:
        print('W array istn string')
    f.close()
