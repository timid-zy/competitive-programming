class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l, r = 0, len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        return letters[l] if letters[l] > target else letters[0]