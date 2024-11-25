for _ in range(int(input())):
    input()
    s = input()
    res = 0
    for i in range(len(s)):
        if i > 0 and s[i] == "#" and s[i-1] == ".":
            res += 1