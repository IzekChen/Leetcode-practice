
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                    
                elif ans:
                    ans.pop()
                    print(ans)
            return "".join(ans)
        return build(S) == build(T)

        



#d = Solution().backspaceCompare("ab##","c#d#")
d = Solution().backspaceCompare("ab#c","ad#c")