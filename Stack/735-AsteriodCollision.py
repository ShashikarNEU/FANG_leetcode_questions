# Monotonic Pattern 
# 3 Cases here [THINK ABOUT THIS!!]
# [-ve] asteriod[i], asteriod[i] and -ve will never meet [IMPOSSIVBLE CASE]
# [+ve] -asteriod[i], this will always meet. so, if asteriod[i] > lot of things in stack -> while loop required and add it to stack
# [+ve] -asteriod[i] so, if asteriod[i] < stack[-1], then nothing will happen, we move on to the next one 
# [+ve] -asteriod[i] if they are same, then ignore the asteriod[i] and pop the stack and move on the next one
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] < abs(asteroids[i]):
                stack.pop()

            if stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] == abs(asteroids[i]):
                stack.pop()
                continue

            if stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] > abs(asteroids[i]):
                continue
            
            stack.append(asteroids[i])
                
        return stack


