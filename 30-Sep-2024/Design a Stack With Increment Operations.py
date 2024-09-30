class CustomStack:

    def __init__(self, maxSize: int):
        self.mx = maxSize
        self.stk = []  
        self.inc = [0] * (maxSize + 1)      

    def push(self, x: int) -> None:
        if len(self.stk) < self.mx:
            self.stk.append(x)

    def pop(self) -> int:
        if len(self.stk) == 0:
            return -1
        
        i = len(self.stk) - 1
        add = self.inc[i]
        if i > 0:
            self.inc[i-1] += add
            
        self.inc[i] = 0
        return self.stk.pop() + add

    def increment(self, k: int, val: int) -> None:
        i = min(len(self.stk), k) - 1
        if i > -1:
            self.inc[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)