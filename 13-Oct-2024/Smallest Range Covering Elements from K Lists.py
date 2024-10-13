class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mnh = []
        mxh = []
        curridx = {}
        for i in range(len(nums)):
            heappush(mnh, (nums[i][0], 0, i))
            heappush(mxh, (-nums[i][0], 0, i))
            curridx[i] = 0
        
        ans = [float('-inf'), float('inf')]
        while True:
            while mxh[0][1] < curridx[mxh[0][2]]:
                _, idx, i = heappop(mxh)
            
            if ans[1] - ans[0] > -mxh[0][0] - mnh[0][0]:
                ans = [mnh[0][0], -mxh[0][0]]
            
            _, idx, i = heappop(mnh)
            idx += 1
            if idx == len(nums[i]):
                break
            
            curridx[i] = idx
            heappush(mnh, (nums[i][idx], idx, i))
            heappush(mxh, (-nums[i][idx], idx, i))
        
        return ans