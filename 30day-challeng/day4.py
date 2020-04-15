#/bin/python3
def moveZeroes(nums):   
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] == 0:
            nums += [nums.pop(i)]
    #print(nums)
    return nums



moveZeroes([0,0,1])