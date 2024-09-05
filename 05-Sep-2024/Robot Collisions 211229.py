# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        def will_collide(first, second):
            return first == "R" and second == "L"
        
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stk = []
        for i in range(len(robots)):
            is_broken = False
            while not is_broken and stk and will_collide(stk[-1][2], robots[i][2]):
                if stk[-1][1] == robots[i][1]:
                    stk.pop()
                    is_broken = True
                
                elif stk[-1][1] < robots[i][1]:
                    robots[i] = (robots[i][0], robots[i][1] - 1, robots[i][2], robots[i][3])
                    stk.pop()
                
                else:
                    stk[-1] = (stk[-1][0], stk[-1][1] - 1, stk[-1][2], stk[-1][3])
                    is_broken = True
            
            if is_broken:
                continue
            
            stk.append(robots[i])
        
        stk.sort(key=lambda x: x[3])
        return list(map(lambda x: x[1], stk))
