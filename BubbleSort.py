def bubbleSort(arr):
    n=len(arr)
    for i in xrange(0,n-1):
        for j in xrange(0,n-1-i):

            print (arr)
            if arr[j] > arr [j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)