class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        dict1 = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        for i in range(len(s)):
            print(dict1.values())
            if s[i] in dict1:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if dict1[open] != s[i]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True