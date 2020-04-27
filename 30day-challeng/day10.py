from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #print(shift)
#        for i in range(len(shift)):
            
#            move = 1 if shift[i][0] == 0 else -1   ### 1:left, -1 right
#            if move == 1 :
#                step = shift[i][1]
#                s = s[step:] + s[:move*step]
#            else:
#                step = shift[i][1] * -1
#                s = s[step:] + s[:len(s) - move* step] 
#            print(step, move* step,s)
#        return s

        for shft in shift:
            direction, amount = shft[0], shft[1]
            if direction == 0: # remove from begining & append to end
                s = s[amount:] + s[:amount]
            elif direction == 1: # remove from end & put it first
                s = s[-amount:] + s[:-amount]
        print(s)
        return s

#s = "abc"
#shift = [[0,1],[1,2]] 

#s = "abcdefg"
#shift = [[1,1],[1,1],[0,2],[1,3]]
#shift = [[1,1]]

s = "joiazl"

shift = [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]

Solution().stringShift(s, shift)
    