class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        inc_stack = []
        sum1 = 0
        for i in range(len(arr)):
            while len(inc_stack) > 0 and inc_stack[-1][0] > arr[i]:
                num, idx = inc_stack.pop()
                if len(inc_stack) > 0:
                    sum1 += (idx - inc_stack[-1][1]) * (i - idx) * num
                else:
                    sum1 += (idx + 1) * (i - idx) * num
            inc_stack.append((arr[i], i))
        
        while len(inc_stack) > 0:
            num, idx = inc_stack.pop()
            if len(inc_stack) > 0:
                sum1 += (idx - inc_stack[-1][1]) * (len(arr) - idx) * num
            else:
                sum1 += (idx + 1) * (len(arr) - idx) * num
        
        return sum1 % (pow(10, 9) + 7)