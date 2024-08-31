class Solution:
    def simplifyPath(self, path: str) -> str:
        
        arr = path.split('/')
        stack = []
        for i in range(len(arr)):
            char = arr[i]
            if char == "" or char == ".":
                continue
            elif char == "..":
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(arr[i])
        
        str1= ""
        for i in stack:
            str1 += "/" + i
        return str1 if str1 != "" else "/"
