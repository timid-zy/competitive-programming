class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            start = 0
            end = len(image[row]) - 1

            while start < end:
                image[row][start], image[row][end] = image[row][end], image[row][start]
                image[row][start] = 1 if image[row][start] == 0 else 0
                image[row][end] = 1 if image[row][end] == 0 else 0
                start += 1
                end -= 1

            mid = len(image[row]) // 2
            if len(image[row]) % 2 == 1:
                image[row][mid] = 1 if image[row][mid] == 0 else 0
        
        return image