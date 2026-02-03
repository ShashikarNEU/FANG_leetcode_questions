# Difference arr + prefix Sum Pattern
# same pattern as Coropate Flight (lc 1094)
# here (first, last) have inc, so, for last+1 index -> subtract inc from the res and at first index -> add inc
# After building the diff arr, iterate and form the prefix arr
# add it to the result
# return (0, length-1) cuz length is given

# we have n+1 here cuz, last+1 means n+1 is possible -> we do n+1
class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        res = [0 for i in range(length+1)]

        for first_index, last_index, inc in updates:
            res[first_index] += inc
            res[last_index+1] -= inc
        
        prefix = []
        curr_inc = 0
        for inc in res:
            curr_inc += inc
            prefix.append(curr_inc)
        
        return prefix[:length]
        


        