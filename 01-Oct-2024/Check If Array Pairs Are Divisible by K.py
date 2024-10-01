class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = Counter()
        for i in range(len(arr)):
            r = arr[i] % k
            t = (k - r) % k
            if rems[t] > 0:
                rems[t] -= 1
            else:
                rems[r] += 1
        
        return not any(rems[k] > 0 for k in rems)
        