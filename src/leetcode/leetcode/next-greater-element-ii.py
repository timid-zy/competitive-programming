class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ret_arr = [-1] * len(nums)
        max_num = max(nums)
        dec_stack = []
        for i in range(len(nums) * 2):
            i = i % len(nums)
            if len(dec_stack) == 0:
                dec_stack.append((nums[i], i))
                continue
            
            while len(dec_stack) > 0 and dec_stack[-1][0] < nums[i]:
                val, idx = dec_stack.pop()
                ret_arr[idx] = nums[i]
            dec_stack.append((nums[i], i))
        
        return ret_arr