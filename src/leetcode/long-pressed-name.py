class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name) or name[-1] != typed[-1]:
            return False
        p_name = 0
        p_typed = 0
        while p_name < len(name) and p_typed < len(typed):
            if name[p_name] != typed[p_typed]:
                return False
            letter_count = 1
            
            for j in range(p_name + 1, len(name)):
                if name[j] == name[j-1]:
                    letter_count += 1
                else:
                    break
            
            typed_count = 0
            while p_typed < len(typed) and name[p_name] == typed[p_typed]:
                typed_count += 1
                p_typed += 1

            if letter_count > typed_count:
                return False

            p_name += letter_count
        if len(typed) > p_typed or len(name) > p_name:
            return False 
        return True