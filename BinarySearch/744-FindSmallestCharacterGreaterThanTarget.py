# Basic binary search with < and res change

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if letters[mid] > target:
                high = mid - 1
                res = mid
            elif letters[mid] <= target:
                low = mid + 1
        
        return letters[res] if res != -1 else letters[0]


        