# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            rarr = mergeSort(arr[mid:])
            larr = mergeSort(arr[:mid])
            return merge(larr, rarr)
        
        def merge(left, right):
            l = r = 0
            ans = []
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    ans.append(left[l])
                    res[left[l][1]] += r
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            
            while l < len(left):
                ans.append(left[l])
                res[left[l][1]] += r
                l += 1

            ans.extend(right[r:])
            return ans
        
        res = [0] * len(nums)
        nums = list(zip(nums, range(len(nums))))
        mergeSort(nums)
        return res