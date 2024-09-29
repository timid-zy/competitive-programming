# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.perim = 2*(width - 1) + 2*(height - 1)
        self.x = self.y = 0
        self.dir = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.names = ["East", "North", "West", "South"]

    def inbound(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def step(self, num: int) -> None:
        dx, dy = self.directions[self.dir]
        num %= self.perim
        if num == 0 and self.x == self.y == 0:
            self.dir = 3

        while num > 0:
            d = 0
            if self.dir == 0:
                d = self.width - self.x - 1
            elif self.dir == 2:
                d = -1 * self.x
            elif self.dir == 1:
                d = self.height - self.y - 1
            else:
                d = -1 * self.y
            
            d = min(abs(d), num)
            num -= d
            if self.dir > 1:
                d *= -1
            
            if self.dir % 2 == 0:
                self.x += d
            else:
                self.y += d   

            if num == 0:
                return
                
            self.dir = (self.dir + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.names[self.dir]        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()