# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1, set2 = set(), set()
        C = []
        for i in range(len(A)):
            for arr in [A, B]:
                if arr[i] in set1:
                    set2.add(arr[i])
                else:
                    set1.add(arr[i])
            
            C.append(len(set2))

        return C