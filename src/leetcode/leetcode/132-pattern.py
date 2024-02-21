class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_arr = [0] * len(nums)
        min_arr[0] = nums[0]
        for i in range(1, len(nums)):
            min_arr[i] = min(min_arr[i - 1], nums[i])
        
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if len(stack) == 0:
                stack.append(nums[i])
                continue
            if nums[i] == stack[-1]: continue
            
            if nums[i] < stack[-1]:
                stack.append(nums[i])
            else:
                prev = None
                if min_arr[i] < stack[-1]:
                    return True

                while len(stack) > 1 and stack[-1] < nums[i]:
                    prev = stack.pop()
                
                if stack[-1] >= nums[i]:
                    stack.append(prev)
                if min_arr[i] < stack[-1]:
                    return True
               
                stack.append(nums[i])
               
        return False     