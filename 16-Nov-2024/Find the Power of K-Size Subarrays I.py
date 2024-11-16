class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cont = 1
        for i in range(1, k-1):
            cont = cont + 1 if nums[i] == nums[i-1] + 1 else 1
        
        ans = []
        for i in range(k-1, len(nums)):
            cont = cont + 1 if nums[i] == nums[i-1] + 1 else 1
            if cont >= k:
                ans.append(nums[i])
            else:
                ans.append(-1)

        return ans