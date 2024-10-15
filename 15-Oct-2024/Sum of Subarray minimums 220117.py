# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(arr) - 1, -1, -1):
            c = 0
            while stk and stk[-1][0] >= arr[i]:
                c += 1
                stk.pop()
            
            v = 0
            if stk:
                v = stk[-1][2] + (stk[-1][1] - i) * arr[i]
            else:
                v = (len(arr) - i) * arr[i]

            res = (res + v) % (10 ** 9 + 7)
            stk.append((arr[i], i, v))
        
        return res
            
