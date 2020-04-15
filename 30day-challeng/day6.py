from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        l = set()
        for i in arr:
            if i not in l:
                l.add(i)
        
        count = 0
        for i in l:
            if i+1 in l:
                times = arr.count(i)
                count += 1 * times
        return count



d = Solution().countElements([1,1,2,2])