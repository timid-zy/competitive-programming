# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target and (mid == 0 or nums[mid - 1] != nums[mid]):
                    return mid
                elif nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != nums[mid]):
                    return mid
                elif nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        return [findLeft(), findRight()]