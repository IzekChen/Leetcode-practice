def maxSubArray(nums):
    if not nums:
        return 0
    current = nums[0]
    m = current
    for i in range(1, len(nums)):
        if current < 0:
            current = 0
        current += nums[i]
        m = max(current, m)
    return m




maxSubArray([1, -2, -1])
maxSubArray([0])
maxSubArray([-1])
maxSubArray([2, 1])


