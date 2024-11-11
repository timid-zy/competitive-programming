# Problem: The Skyline Problem - https://leetcode.com/problems/the-skyline-problem/

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = []
        res = []
        for l, r, h in buildings:
            while heap and heap[0][2] < l:
                oh, ol, oR = heappop(heap)
                while heap and heap[0][2] <= oR:
                    heappop(heap)
                
                if not heap:
                    res.append([oR, 0])

                elif heap[0][2] > oR:
                    res.append([oR, -heap[0][0]])
            
            if not heap or -heap[0][0] < h:
                res.append([l, h])
            
            heappush(heap, (-h, l, r))
        
        while heap:
            oh, ol, oR = heappop(heap)
            while heap and heap[0][2] <= oR:
                heappop(heap)
            
            if not heap:
                res.append([oR, 0])

            elif heap[0][2] > oR:
                res.append([oR, -heap[0][0]])

        invalid = set()
        for i in range(1, len(res)):
            if res[i][1] == res[i-1][1]:
                invalid.add(i)
            
            if res[i][0] == res[i-1][0]:
                invalid.add(i-1)
        
        ans = []
        for i in range(len(res)):
            if i not in invalid:
                ans.append(res[i])

        return ans
