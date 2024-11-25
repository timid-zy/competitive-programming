for _ in range(int(input())):
    input()
    s = input()
    curr = mx = 0
    for i in range(len(s)):
        if s[i] == ".":
            curr += 1
            mx = max(curr, mx)
            continue
        
        curr = 0
    
    if mx > 2:
        print(2)
    else:
        print(s.count("."))

        