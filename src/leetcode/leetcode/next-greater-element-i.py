class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dec_stack = []
        dict1 = {}

        for i in range(len(nums2)):
            if len(dec_stack) == 0:
                dec_stack.append(nums2[i])
                continue
            
            while len(dec_stack) != 0 and dec_stack[-1] < nums2[i]:
                dict1[dec_stack.pop()] = nums2[i]
            dec_stack.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = dict1.get(nums1[i], -1)
        return nums1