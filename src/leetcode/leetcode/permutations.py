class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(arr):
            if len(arr) == len(nums):
                permutations.append(arr)
                return
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    backtrack(arr + [nums[i]])
        
        permutations = []      
        backtrack([])
        return permutations
            