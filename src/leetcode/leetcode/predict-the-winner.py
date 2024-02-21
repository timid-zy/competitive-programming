class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def calcScore(start, end, flag):
            if start >= end:
                return 0

            if not flag:
                p21 = calcScore(start + 1, end, False) + nums[start]
                p22 = calcScore(start, end - 1, False) + nums[end]
                if p21 > p22:
                    start += 1
                else:
                    end -= 1
            
            s1 = calcScore(start + 1, end, False) + nums[start]
            s2 = calcScore(start, end - 1, False) + nums[end]
            return max(s1, s2)

        if len(nums) == 1: return True
        playerOne = calcScore(0, len(nums) - 1, True)
        playerTwo = sum(nums) - playerOne
        return playerOne >= playerTwo