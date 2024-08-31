class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_ = 0
        stack = []
        for i in range(len(heights)):
            count = 0
            while stack and stack[-1][0] >= heights[i]:
                popped = stack.pop()
                count += popped[1]
                max_ = max(max_, count * popped[0])
            
            stack.append((heights[i], count + 1))
        
        count = 0
        while stack:
            popped = stack.pop()
            count += popped[1]
            max_ = max(max_, count * popped[0])
        
        return max_