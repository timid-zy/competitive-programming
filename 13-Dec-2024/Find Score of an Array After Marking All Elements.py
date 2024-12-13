class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        arr = sorted(list(zip(nums, range(len(nums)))))
        score = 0
        for n, i in arr:
            if i in marked:
                continue
            
            score += n
            marked.add(i)
            if i-1 >= 0:
                marked.add(i-1)
            if i+1 < len(nums):
                marked.add(i+1)

            if len(marked) == len(nums):
                return score