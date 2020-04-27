#/bin/python

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        print(profit)


d = Solution().maxProfit([7,1,5,3,6,4])


d = Solution().maxProfit([1,2,3,4,5])
d = Solution().maxProfit([7,6,4,3,1])