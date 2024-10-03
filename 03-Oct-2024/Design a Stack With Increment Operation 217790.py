# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.mx = maxSize
        self.stk = []
        self.inc = [0] * (self.mx)

    def push(self, x: int) -> None:
        if len(self.stk) < self.mx:
            self.stk.append(x)

    def pop(self) -> int:
        if len(self.stk) == 0:
            return -1

        idx = len(self.stk) - 1
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]

        ans = self.stk.pop() + self.inc[idx]
        self.inc[idx] = 0
        return ans

    def increment(self, k: int, val: int) -> None:
        if len(self.stk) == 0:
            return 
        
        if k > len(self.stk):
            self.inc[len(self.stk) - 1] += val
        else:
            self.inc[k-1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)