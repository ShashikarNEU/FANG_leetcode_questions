# Logic - Use Stack
# when you encounter .. , pop the stack 
# if .. in the start, ignore it
# if "" and "." in the array, ignore it

# EDGE CASE: Think about .. in the start(use continue, ignore it) -> it's not valid path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        print(paths)

        for curr in paths:
            if curr == ".." and stack:
                stack.pop()
            elif curr == ".." and not stack:
                continue
            elif curr != "." and curr != "":
                stack.append(curr)
        
        return "/" + "/".join(stack)