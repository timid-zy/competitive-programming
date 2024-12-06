class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        res = 0
        sum_ = 0
        for i in range(1, n+1):
            if i in ban:
                continue
            
            sum_ += i
            if sum_ > maxSum:
                return res
            
            res += 1
        
        return res
        