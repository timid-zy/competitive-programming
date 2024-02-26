class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtrack(arr, idx=0):
            ret.append(arr)
            for i in range(idx, len(nums)):
                backtrack(arr + [nums[i]] , i + 1)

        backtrack([])
        return ret