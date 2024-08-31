class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_num = 1001
        max_num = -1
        for num, fromL, toL in trips:
            max_num = max(max_num, fromL, toL)
            min_num = min(min_num, fromL, toL)

        prefix = [0] * (max_num - min_num + 3)
        for num, fromL, toL in trips:
            prefix[fromL - min_num + 1] += num
            prefix[toL - min_num + 1] -= num
        
        # compute the prefix sum
        for i in range(len(prefix)):
            prefix[i] += prefix[i - 1]
            if prefix[i] > capacity:
                return False
        return True


