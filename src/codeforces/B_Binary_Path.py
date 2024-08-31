for i in range(int(input())):
    input()
    s1 = input()
    s2 = input()

    if len(s1) == 1:
        print(1)
        continue

    p1 = 1
    p2 = 0

    curr = s1[0]
    candidates = []

    while p1 < len(s1):
        # add to list of possible answers
        if s1[p1] == s2[p2]:
            candidates.append( len(curr) - 1)
            curr += s1[p1]
        
        elif s1[p1] < s2[p2]:
            curr += s1[p1]

        else:
            curr += s2[len(curr) - 1:-1]
            break
            
        p1 += 1
        p2 += 1
    curr += s2[-1]
    print(curr)
    
    count = 1
    for j in range(len(candidates)):
        flag = True
        for i in range(candidates[j], len(s2)):
            if s2[i] != curr[i + 1]:
                flag = False
                break
        if flag:
            count += len(candidates) - j
            break

    print(count)