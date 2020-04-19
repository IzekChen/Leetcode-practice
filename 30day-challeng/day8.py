from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones = sorted(stones, reverse=True)
        print('len of stones: ' + str(len(stones)))
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            print(stones)
            if stones[0] > stones[1]:
                stones.append( stones[0] - stones[1] )
                stones = stones[2:]
            elif stones[0] < stones[1]:
                stones.append( stones[1] - stones[0] )
                stones = stones[2:]
            else:
                stones = stones[2:]
        print(stones)
        
        print(stones[0]) if stones else print('0')
        return stones[0] if stones else 0




                



#d = Solution().lastStoneWeight([2,7,4,1,8,1])
#d = Solution().lastStoneWeight([2,2])
d = Solution().lastStoneWeight([1,3])