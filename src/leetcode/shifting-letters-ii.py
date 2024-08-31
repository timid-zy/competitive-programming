class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        operations = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            
            if direction == 0:
                operations[start] -= 1
                operations[end + 1] += 1
            elif direction == 1:
                operations[start] += 1
                operations[end + 1] -= 1
        
        # compute prefix
        for i in range(1, len(operations)):
            operations[i] += operations[i - 1]
            
        ret_str = ""
        for i in range(len(s)):
            idx = ord(s[i]) % 97
            idx += operations[i]
            idx = idx % 26
            ret_str += chr(idx + 97)
        
        return ret_str