# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, OP: List[str]) -> int:
        stack = []
        for i in range(len(OP)):
            if OP[i] == "+":
                stack.append(stack[-1] + stack[-2])
            
            elif OP[i] == "D":
                stack.append(stack[-1] * 2)
            
            elif OP[i] == "C":
                stack.pop()

            else:
                stack.append(int(OP[i]))
        
        return sum(stack)