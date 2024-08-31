class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        count = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in count: count[nums[i]] += 1
            else: count[nums[i]] = 1

        for i in range(len(nums)):
            curr = nums[i]
            if count[nums[i]] <= 0:
                continue
    
            for j in range(k):
                if curr + j not in count or count[curr + j] <= 0:
                    return False
                count[curr + j] -= 1

        return True
            

