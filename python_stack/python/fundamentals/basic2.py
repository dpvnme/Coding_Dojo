# def printReturn(lst):
#     print(lst[1])
#     return lst[0]
# print(printReturn([1,2]))

# def firstLength(lst):
#     sum = len(lst)+lst[0]
#     return sum
# print(firstLength([1,2,3,4,5]))

# def valGreaterSecond(lst):
#     if len(lst) < 2:
#         return -1
#     else:
#         temp = lst[1]
#         counter = 0
#         lst2 = []
#         for i in range (0,len(lst)):
#             if (lst[i]>temp):
#                 lst2.append(lst[i])
#                 counter += 1
#         print(counter, lst2)
# valGreaterSecond([5])

def lengthValue(size, value):
    lst = []
    for i in range (0,size):
        lst.append(value)
    print(lst)
lengthValue(12,3)
