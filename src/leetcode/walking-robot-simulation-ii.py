class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.loop = self.width * 2 + self.height * 2
        self.x = 0
        self.y = 0
        self.dir = "East"

    def step(self, num: int) -> None:
        num = num % self.loop
        if num == 0 and self.x == self.y and self.x == 0: self.dir = "South"
        unfinished = True
        
        while unfinished and num > 0:
            if self.dir == "East":
                newPos = self.x + num
                if newPos > self.width:
                    num -= self.width - self.x
                    self.x = self.width
                    self.dir = "North"
                else:
                    self.x = newPos
                    unfinished = False

            elif self.dir == "West":
                newPos = self.x - num
                if newPos < 0:
                    num -= self.x
                    self.x = 0
                    self.dir = "South"
                else:
                    self.x = newPos
                    unfinished = False
        
            elif self.dir == "North":
                newPos = self.y + num
                if newPos > self.height:
                    num -= self.height - self.y
                    self.y = self.height
                    self.dir = "West"
                else:
                    self.y = newPos
                    unfinished = False
            
            elif self.dir == "South":
                newPos = self.y - num
                if newPos < 0:
                    num -= self.y
                    self.y = 0
                    self.dir = "East"
                else:
                    self.y = newPos
                    unfinished = False
        
        # if self.dir == "West" and self.x == 0:
        #     self.dir = "South"
        # if self.dir == "South" and self.y == 0:
        #     self.dir = "East"
        # if self.dir == "North" and self.y == self.height:
        #     self.dir = "West"
        # if self.dir == "East" and self.x == self.width:
        #     self.dir = "North"
        # print(num, ":", self.x, self.y)

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        
    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()