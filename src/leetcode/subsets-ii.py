class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def subsets(arr, idx):
            nonlocal subs
            subs.append(arr)
            visited = set()
            for i in range(idx, len(nums)):
                pre_len = len(visited)
                visited.add(nums[i])
                if len(visited) != pre_len:
                    subsets(arr + [nums[i]], i + 1)
        
        subs = []
        subsets([], 0)
        return subs