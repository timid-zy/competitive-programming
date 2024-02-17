class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        nums2_dict = {}

        for i in range(len(nums1)):
            if nums1[i] not in nums1_dict:
                nums1_dict[nums1[i]] = 1
            else:
                nums1_dict[nums1[i]] += 1
        
        for j in range(len(nums2)):
            if nums2[j] not in nums2_dict:
                nums2_dict[nums2[j]] = 1
            else:
                nums2_dict[nums2[j]] += 1
        
        intersection_arr = []
        for key in nums1_dict:
            if key not in nums2_dict:
                continue
            occurence = min(nums1_dict[key], nums2_dict[key])
            intersection_arr += [key] * occurence
        
        return intersection_arr