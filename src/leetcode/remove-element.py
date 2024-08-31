class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valPos = None
        try:
            valPos = nums.index(val)
        except:
            return len(nums)

        end = len(nums) - 1
        while end >= 0 and nums[end] == val:
            end -= 1
        
        while valPos <= end:
            if nums[valPos] == val:
                nums[end], nums[valPos] = nums[valPos], nums[end]
                end -= 1
                while end >= 0 and nums[end] == val:
                    end -= 1
                valPos += 1
            else:
                valPos += 1

        return len(nums) - nums.count(val)