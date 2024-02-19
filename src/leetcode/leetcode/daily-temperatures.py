class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        dec_stack = []
        arr = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(temperatures) == 0: 
                dec_stack.append((temperatures[i], i))
                continue
            
            while len(dec_stack) > 0 and dec_stack[-1][0] < temperatures[i]:
                temp, idx = dec_stack.pop()
                arr[idx] = i - idx

            dec_stack.append((temperatures[i] , i))

        return arr