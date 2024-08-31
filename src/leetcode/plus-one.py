class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        i = -1
        while i > -1 * len(digits):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        
        if digits[0] < 9:
            digits[0] += 1
        else:
            digits[0] = 0
            digits.insert(0, 1)
        
        return digits