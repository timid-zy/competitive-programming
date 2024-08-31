class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        closest = sum(nums[:3])
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                
                if curr_sum < target:
                    start += 1
                else:
                    end -= 1
        

        return closest