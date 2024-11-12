class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        mxs = [0] * len(items)
        mxs[0] = items[0][1]
        for i in range(1, len(items)):
            mxs[i] = max(items[i][1], mxs[i-1])
        
        res = []
        for q in queries:
            if q < items[0][0]:
                res.append(0)
                continue
            
            l, r = 0, len(mxs)-1
            while l < r:
                mid = (r + l + 1) // 2
                if items[mid][0] > q:
                    r = mid - 1
                else:
                    l = mid
            
            res.append(mxs[l])
        
        return res