class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def getSign(num):
            return -1 if num < 0 else 1
        nums.sort(key=getSign)
        
        newArr = [0] * len(nums)
        mid = len(nums) // 2
        j = 0
        for i in range(0, len(nums), 2):
            newArr[i + 1] = nums[j]
            newArr[i] = nums[mid + j]
            j += 1

        return newArr