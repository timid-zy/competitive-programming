# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        res = 0
        for i, h in enumerate(heights):
            c = 0
            while stk and stk[-1][0] >= h:
                oh, oi = stk.pop()
                c += oi
                res = max(res, c * oh)
            
            stk.append((h, c+1))
        
        c = 0
        while stk:
            oh, oi = stk.pop()
            c += oi
            res = max(res, c * oh)
        
        return res