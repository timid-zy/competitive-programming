ret_str = ""
for i in range(int(input())):
    arr = []
    for char in input():
        arr.append(char)
    pos = int(input())

    max_char = arr[i]
    max_idx = 0

    i = 0
    while i < pos:
        actual_pos = pos % len(arr)
        
        if max_char is None or max_char 

