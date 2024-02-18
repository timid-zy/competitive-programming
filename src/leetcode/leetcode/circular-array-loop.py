class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            indicies = set()
            # indicies.add(i)
            j = i
            isPos = nums[j] > 0
            for _ in range(len(nums) + 1):
                if (nums[j] > 0 and not isPos) or (nums[j] < 0 and isPos):
                    break
                if (j in indicies) and j == i and len(indicies) > 1: 
                    # print(j, indicies)
                    return True
                indicies.add(j)
                j = (j + nums[j]) % len(nums)
        
        return False