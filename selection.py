def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1, n-1):
            if arr[j] < arr[min_index]:
                temp = arr[min_index]
                arr[min_index]=arr[j]
                arr[j]=temp
        print(arr)
arr = [3, 1, 41, 59, 26, 53, 59]
selection_sort(arr)

