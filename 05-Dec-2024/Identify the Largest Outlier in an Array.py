class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = sum(nums)
        outlier = float('-inf')
        for i in range(len(nums)):
            if (total - nums[i]) % 2 == 1:
                continue

            counter[nums[i]] -= 1
            special1 = (total - nums[i]) // 2
            if counter[special1] > 0:
                outlier = max(outlier, nums[i])

            counter[nums[i]] += 1
        
        return outlier
