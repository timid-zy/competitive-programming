# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], ID: int, VD: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j) >= ID and abs(nums[i] - nums[j]) >= VD:
                    return [i, j]
        
        return [-1, -1]