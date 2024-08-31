class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            temp = heights[i]
            name = names[i]
            j = i - 1
            while j >= 0 and heights[j] <  temp:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j + 1] = temp
            names[j + 1] = name
        return names