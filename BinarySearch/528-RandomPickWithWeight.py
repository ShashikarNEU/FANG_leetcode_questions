# Tricky question
# Brute force -> have as many as the val of the number in the arr and pick randomly
# eg:- [1,3] have a arr with [1,3,3,3] and pick. but with large numbers, it won't work

# So, to optimize it, use prefix sum method. then, use find random number and search for the random number within prefix
# using binary search and return the index(USE CODN TARGET <= PREFIX[i])

# THINK using example and reference video -> https://www.youtube.com/watch?v=cw826XIOZIg
import random
class Solution:
    def __init__(self, w: list[int]):
        # form the prefix sum arr here
        self.prefix = []
        self.sum = 0
        for num in self.w:
            self.sum+=num
            self.prefix.append(self.sum)
            
    def pickIndex(self) -> int:
        target = random.randint(1, self.sum)
        low = 0
        high = len(self.prefix)-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if self.prefix[mid] >= target:
                high = mid - 1
                res = mid
            elif self.prefix[mid] < target:
                low = mid + 1
                
        return res

# Variant alert 
# you are given a [city, population] arr. if we pick a random person which city is he from?
# Same problem but different words