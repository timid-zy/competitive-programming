class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]

        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if tokens[i] == '+': res = num1 + num2 
                if tokens[i] == '-': res = num1 - num2 
                if tokens[i] == '*': res = num1 * num2 
                if tokens[i] == '/': res = int(num1 / num2)
                stack.append(res)
        return stack[0]