def bubbleSort(arr):
    temp = len(arr)-1
    print(arr)
    for j in range (temp):
        for i in range(temp-j):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        print(arr)

bubbleSort([4,1,3,2]*10)