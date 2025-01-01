# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if mid > 0 and arr[mid-1] > arr[mid]:
                r = mid - 1
            elif mid < len(arr) and arr[mid+1] > arr[mid]:
                l = mid + 1
            else:
                return mid
        
        return l