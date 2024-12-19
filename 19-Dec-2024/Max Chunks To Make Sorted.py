class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s1, s2 = set(), set()
        c = 0
        for i in range(len(arr)):
            if arr[i] <= i:
                s1.add(arr[i])
            else:
                s2.add(arr[i])
            
            if i in s2:
                s2.remove(i)
                s1.add(i)

            if len(s2) == 0 and len(s1) > 0:
                c += 1
                s1, s2 = set(), set()
        
        return c