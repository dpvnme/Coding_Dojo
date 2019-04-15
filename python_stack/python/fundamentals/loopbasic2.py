# def biggieSize(lst):
#     for i in range (len(lst)):
#         if (lst[i]<0):
#             lst[i] = "big"
#     print(lst)
# biggieSize([-1,0,4,1,-6])

# def countPositive(lst):
#     temp = 0
#     for i in range (len(lst)):
#         if(lst[i]>0):
#             temp+=1
#     lst[len(lst)-1] = temp
#     print(lst)
# countPositive([1,2,-3,-4,-5])

# def sumTotal(lst):
#     sum = 0
#     for i in range (len(lst)):
#         sum = sum + lst[i]
#     print(sum)
# sumTotal([1,2,3,4,5])

# def avgTotal(lst):
#     sum = 0
#     avg = 0
#     for i in range (len(lst)):
#         sum = sum + lst[i]
#     avg = sum / len(lst)
#     print(avg)
# avgTotal([1,2,3,4])

def reverseList(lst):
    temp = 0
    if (len(lst)%2==0):
        print("Even list")
        for i in range (int(len(lst)/2)):
            temp = lst[len(lst)-1-i]
            lst[len(lst)-1-i] = lst[i]
            lst[i] = temp
    else:
        print("Odd list")
        for i in range (int(len(lst)/2)):
            temp = lst[len(lst)-1-i]
            lst[len(lst)-1-i] = lst[i]
            lst[i] = temp
    print(lst)
reverseList([1,2,3,4,5])

        