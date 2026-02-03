# No Hint
# Easy, just THINK
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        count = 0
        for bracket in s:
            if bracket == '(':
                open+=1
            elif bracket == ')':
                open-=1
            
            if open < 0:
                open = 0
                count+=1
        
        count += open
        return count

        