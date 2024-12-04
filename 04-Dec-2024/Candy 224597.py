# Problem: Candy - https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = sorted(list(zip(ratings, range(len(ratings)))))
        res = [1] * len(ratings)
        for _, idx in arr:
            if idx > 0 and ratings[idx-1] < ratings[idx]:
                res[idx] = max(res[idx], res[idx-1] + 1)
            
            if idx < len(arr)-1 and ratings[idx+1] < ratings[idx]:
                res[idx] = max(res[idx], res[idx+1] + 1)
        
        return sum(res)