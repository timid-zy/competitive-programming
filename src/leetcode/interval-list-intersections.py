class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            left_most = max(firstList[i][0], secondList[j][0])
            right_most = min(firstList[i][1], secondList[j][1])

            if left_most <= right_most:
                ans.append([left_most, right_most])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans