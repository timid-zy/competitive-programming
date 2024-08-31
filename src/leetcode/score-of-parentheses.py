class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        score = 0
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(char)
            else:
                if stack[-1] != "(":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    stack.pop()
                    stack.append(num * 2)
                else:
                    stack.pop()
                    stack.append(1)
            
            if isinstance(stack[0], int):
                score += stack.pop()
        
        return score