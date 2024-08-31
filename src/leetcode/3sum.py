class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retArr = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum_all = nums[i] + nums[start] + nums[end]
                if sum_all == 0:
                    retArr.append([ nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif sum_all > 0:
                    end -= 1
                else:
                    start += 1

        return retArr