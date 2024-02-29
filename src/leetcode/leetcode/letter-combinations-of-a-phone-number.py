class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combos = []
        def getCombinations(letters, idx=0):
            if len(letters) == len(digits):
                combos.append(letters)
                return
            
            for char in chars[digits[idx]]:
                getCombinations(letters + char, idx + 1)

        if len(digits) == 0: return []
        getCombinations("")
        return combos