class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        mx = 0
        # T
        start = 0
        ops = k
        for end in range(len(answerKey)):
            if answerKey[end] == "F" and ops > 0:
                ops -= 1
            elif answerKey[end] == "F" and ops == 0:
                mx = max(mx, end - start)
                while answerKey[start] == "T":
                    start += 1
                start += 1
        mx = max(mx, len(answerKey) - start)
    
        # F
        start = 0
        ops = k
        for end in range(len(answerKey)):
            if answerKey[end] == "T" and ops > 0:
                ops -= 1
            elif answerKey[end] == "T" and ops == 0:
                mx = max(mx, end - start)
                while answerKey[start] == "F":
                    start += 1
                start += 1
        mx = max(mx, len(answerKey) - start)
                
        
        return mx
