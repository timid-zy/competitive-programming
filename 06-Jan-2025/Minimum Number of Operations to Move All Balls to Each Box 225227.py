# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        r = rc = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                r += i
                rc += 1
            
        l = lc = 0        
        res = [0] * len(boxes)
        res[0] = r
        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                lc += 1
                rc -= 1
            
            r -= rc
            l += lc
            res[i] = l + r
        
        return res