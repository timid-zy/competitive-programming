# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def customSort(a):
            arr, idx = a
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            return arr[1]
        
        def bisectRight(arr, n):
            if len(arr) == 0 or arr[0][0] <= n: return -1
            if n < arr[-1][0]: return arr[-1][1]
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r + 1) // 2
                if n < arr[mid][0]:
                    l = mid
                else:
                    r = mid - 1
                
            return arr[l][1]
                    
        queries = list(zip(queries, range(len(queries))))
        ans = [-1] * len(queries)
        queries.sort(key=customSort, reverse=True)
        stack = []
        end = len(heights) - 1
        for (l, r), idx in queries:
            while r < end and end >= 0:
                while end > 0 and stack and stack[-1][0] <= heights[end]:
                    stack.pop()

                stack.append((heights[end], end))
                end -= 1

            if heights[l] < heights[r] or l == r:
                ans[idx] = r
            elif heights[l] == -1 or heights[r] == -1:
                ans[idx] = -1
            else:
                ans[idx] = bisectRight(stack, max(heights[l], heights[r]))
            
        return ans