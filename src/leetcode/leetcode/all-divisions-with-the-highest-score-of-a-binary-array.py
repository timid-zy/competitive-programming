class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroes = [0] * (len(nums) + 1)
        ones = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes[i + 1] = zeroes[i] + 1
            else:
                zeroes[i + 1] = zeroes[i]
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                ones[i] = ones[i + 1] + 1
            else:
                ones[i] = ones[i + 1]

        max_score = 0
        max_score_idx = []
        
        for i in range(len(zeroes)):
            if max_score < zeroes[i] + ones[i]:
                max_score = zeroes[i] + ones[i]
                max_score_idx = [i]
            elif max_score == zeroes[i] + ones[i]:
                max_score_idx.append(i)
        
        return max_score_idx
