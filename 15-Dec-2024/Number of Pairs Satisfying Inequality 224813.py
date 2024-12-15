# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            nonlocal count, req
            r = 0
            for i in range(len(left)):
                while r < len(right) and right[r][0] <= req[left[i][1]]: r += 1
                count += r
            
            l = r = 0
            res = []
            while l < len(left) and r < len(right):
                if left[l][0] < right[r][0]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            
            res.extend(left[l:])
            res.extend(right[r:])
            return res
            
        req = []
        search = []
        for i in range(len(nums1)):
            req.append(diff + (nums2[i] - nums1[i]))
            search.append((nums2[i] - nums1[i], i))

        count = 0
        mergeSort(search)
        return count
        