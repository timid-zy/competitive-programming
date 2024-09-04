class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        O = set([(x, y) for x, y in obstacles])
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)] # r= +1, l = -1
        cx = cy = di = 0
        res = 0
        for n in commands:
            if n == -1:
                di = (di + 1) % len(dire)
                continue
            elif n == -2:
                di = (di - 1) % len(dire)
                continue
            
            for _ in range(n):
                nx, ny = cx + dire[di][0], cy + dire[di][1]
                if (nx, ny) in O:
                    break
                
                cx, cy = nx, ny
                res = max(
                    res,
                    (cx**2 + cy**2)
                )
        
        return res
        