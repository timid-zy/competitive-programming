class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        ret_str = ""
        changed = False
        for i in range(len(palindrome)):
            if palindrome[i] != "a" and not changed:
                ret_str += "a"
                changed = True
            else:
                ret_str += palindrome[i]

        return ret_str if changed and ret_str != ret_str[::-1] else palindrome[:-1] + "b"
