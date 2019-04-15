def selectionSort(lst):
    highIndex = len(lst)-1
    highValue = lst[highIndex]
    print(highIndex, highValue)
    for j in range (len(lst)):
        for i in range (len(lst)-j):
            if (lst[i]>highValue):
                highValue = lst[i]
                highIndex = i
            # print("after if",highIndex, highValue)
        lst[len(lst)-1], lst[highIndex] = lst[highIndex], lst[len(lst)-1]
        print(lst)
# selectionSort([1,3,6,4,4,9,4,-1,1])
selectionSort([1,3,2])
