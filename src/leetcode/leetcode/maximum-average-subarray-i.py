class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = sum(nums[:k]) / k
        prevAvg = maxAvg
        for right in range(k, len(nums)):
            currAvg = prevAvg - nums[right-k]/k + nums[right]/k
            prevAvg = currAvg
            if currAvg > maxAvg:
                maxAvg = currAvg
        
        return maxAvg