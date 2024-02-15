class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        nums.sort()
        count = 0
        _dict = {nums[0] + nums[1]: 1}
        for i in range(2, len(nums)):
            if nums[i] == 0: continue
            for key in _dict:
                if key > nums[i]:
                    count += _dict[key]

            for j in range(i):
                if nums[j] == 0: continue
                key = nums[i] + nums[j]
                if key in _dict:
                    _dict[key] += 1
                else:
                    _dict[key] = 1


        return count