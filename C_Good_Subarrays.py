for i in range(int(input())):
    input()
    s = input()
    
    r_sum = 0
    seen = {}
    count = 0
    for i in range(len(s)):
        num = int(s[i])
        old = r_sum - i + 1
        if old in seen:
            seen[old] += 1
        else:
            seen[old] = 1
        r_sum += num
        curr = r_sum - i

        if curr in seen:
            count += seen[curr]
    
    print(count)