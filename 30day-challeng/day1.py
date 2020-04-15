#bin/python3
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Note:

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Example 1:

#Input: [2,2,1]
#Output: 1
#Example 2:

#Input: [4,1,2,1,2]
#Output: 4


def findSingle( ar, n):
    res = ar[0]

    for i in range(1,n):
        res = res ^ ar[i]
    return res


lists = [2, 2, 1]
print(findSingle(lists, len(lists)))
