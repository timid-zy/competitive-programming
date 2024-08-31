class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ops = []
        for i in range(len(arr) - 1, -1, -1):
            max_num = arr[0]
            max_idx = 0
            for j in range(1, i + 1):
                if arr[j] >= max_num:
                    max_idx = j
                    max_num = arr[j]
            if max_idx == i: continue

            rotated = arr[0:max_idx + 1]
            arr = rotated[::-1] + arr[max_idx + 1:]
            ops.append(max_idx + 1)
            rotated2 = arr[0:i+1]
            arr = rotated2[::-1] + arr[i+1:]
            ops.append(i + 1)       
        return ops
