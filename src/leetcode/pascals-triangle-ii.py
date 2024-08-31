class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascalTriangle(idx, num):
            if idx == rowIndex:
                return num
            
            arr = [1]
            for i in range(1, len(num)):
                arr.append(num[i] + num[i - 1])
            arr.append(1)
            return pascalTriangle(idx + 1, arr)
        

        return pascalTriangle(0, [1])