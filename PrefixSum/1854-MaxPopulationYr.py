# Diff arr + prefix sum Pattern
# same as lc 1109, 1094, 370
# we should (1950,2050) to arr starting from zero so, we do res[birth or death -1950], we get 0 to 1000 arr
class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        res = [0] * 1001

        for birth, death in logs:
            res[birth-1950]+=1
            res[death-1950]-=1
        
        max_ppl = float('-inf')
        currPpl = 0
        res_ppl = []
        ans = 0

        for i, ppl in enumerate(res):
            currPpl += ppl
            res_ppl.append(currPpl)
            if currPpl > max_ppl:
                max_ppl = currPpl
                ans = i
    
        return ans+1950