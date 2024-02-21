class Solution:
    def trap(self, height: List[int]) -> int:
        
        inc_stack = []
        units = 0
        covered = 0
        for i in range(len(height)):
            if len(inc_stack) == 0:
                if height[i] != 0: inc_stack.append(height[i])
                continue
            
            if height[i] < inc_stack[0]:
                inc_stack.append(height[i])
                covered += height[i]
            
            elif height[i] >= inc_stack[0]:
                units += min(inc_stack[0], height[i]) * (len(inc_stack) - 1) - covered
                inc_stack = [height[i]]
                covered = 0
        
        covered = 0
        stack2 = []
        for i in range(len(inc_stack) - 1, -1, -1):
            if len(stack2) == 0:
                if inc_stack[i] != 0: stack2.append(inc_stack[i])
                continue
            
            if inc_stack[i] < stack2[0]:
                stack2.append(inc_stack[i])
                covered += inc_stack[i]
            
            elif inc_stack[i] >= stack2[0]:
                # print(units, stack2)
                units += min(stack2[0], inc_stack[i]) * (len(stack2) - 1) - covered
                stack2 = [inc_stack[i]]
                covered = 0
                # print(units, stack2)

        return units

            

            