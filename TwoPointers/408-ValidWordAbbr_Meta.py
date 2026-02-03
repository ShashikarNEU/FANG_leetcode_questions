# Here, you can use a hashMap or a arr to store word's letters and index
# then compare with abbr

# But if we want the SC to be const, use two pointers
# have t1 and t2 and while codn(t1<len(word) and t2<len(abbr))
# if abbr[t2] is a digit, collect all digits, do t1+=digits and in the iteration
# compare it with word[t1]==abbr[t2]

# IMP Edge Case: if after the end of the while loop t1 and t2 has to be at length+1 in indexes
# eg:- word='a' and abbr='2'
# After the loop, t1 is at index 2 and t2 is at index 1. no FALSE is triggered so, when return True, see if
# t1 == len(word) and t2 == len(abbr)
# EDGE CASE 2: when checking digit, t2 has to be inside len(abbr)

# Iterative Version using two pointers
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        t1 = 0
        t2 = 0
    
        while t1 < len(word) and t2 < len(abbr):
            if abbr[t2] == '0':
                return False
            
            count = ""
            if abbr[t2].isdigit():
                while t2 < len(abbr) and abbr[t2].isdigit():
                    count += abbr[t2]
                    t2+=1
    
                t1+=int(count)
            else:
                if word[t1] != abbr[t2]:
                    #print(word[t1],abbr[t2])
                    return False
                t1+=1
                t2+=1
              
        return t1 == len(word) and t2 == len(abbr)       

# Recursive Version using two pointers
# Find every False codn and return FALSE. After you return True. progate the true up the call stack
# if t2 >= len(abbr) or t1 >= len(word): return False is the EDGE CASE HERE. if t2 == len(abbr) and t1 == len(word) is the TRUE Codn
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def recursive_validWordAbbr(t1, t2):
            if t2 == len(abbr) and t1 == len(word):
                return True
            
            if t2 >= len(abbr) or t1 >= len(word):
                return False
            
            if abbr[t2].isdigit():
                if abbr[t2] == '0':
                    return False
                count = ""
                while t2 < len(abbr) and abbr[t2].isdigit():
                    count += abbr[t2]
                    t2+=1
                if int(count) > len(word):
                    return False
                
                return recursive_validWordAbbr(t1+int(count),t2)
            
            if word[t1] != abbr[t2]:
                return False
            return recursive_validWordAbbr(t1+1,t2+1)
        
        return recursive_validWordAbbr(0, 0)

# Variant Question : what if we have a wild card version 

# Example
# word = h e l z z p m e
# abbr = h 2 * p * m e

# * can mean any number from 0 to anything

# Reference Video -> https://www.youtube.com/watch?v=ALDB1fi65U8

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def recursive_validWordAbbr(t1, t2):
            if t2 == len(abbr) and t1 == len(word):
                return True
            
            if t2 >= len(abbr) or t1 >= len(word):
                return False
            
            if abbr[t2].isdigit():
                if abbr[t2] == '0':
                    return False
                count = ""
                while t2 < len(abbr) and abbr[t2].isdigit():
                    count += abbr[t2]
                    t2+=1
                if int(count) > len(word):
                    return False
                
                return recursive_validWordAbbr(t1+int(count),t2)
            
            # Only Difference here is this
            # Watch video or visualize this with example
            if abbr[t2] == '*':
                recursive_validWordAbbr(t1, t2+1)
                recursive_validWordAbbr(t1+1, t2)
                
            if word[t1] != abbr[t2]:
                return False
            return recursive_validWordAbbr(t1+1,t2+1)
        
        return recursive_validWordAbbr(0, 0)