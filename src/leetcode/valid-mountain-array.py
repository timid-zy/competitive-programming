class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        
        str_inc = False
        if arr[0] < arr[1]:
            str_inc = True
        else:
            return False
        str_dec = False

        for i in range(2, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            
            if arr[i] > arr[i - 1] and not str_inc:
                return False
            if arr[i] < arr[i - 1] and str_inc:
                str_dec = True
                str_inc = False
            elif arr[i] < arr[i - 1] and not str_dec:
                return False
        
        return True if str_dec else False