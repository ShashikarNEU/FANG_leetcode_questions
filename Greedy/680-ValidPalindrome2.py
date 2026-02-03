# Instead of backtracking, use sub function check palindrome

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(start, end):
            while start <= end:
                if s[start] == s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            
            return True
        
        start = 0
        end = len(s)-1

        while start <= end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return checkPalindrome(start+1, end) or checkPalindrome(start, end-1)
        
        return True

        