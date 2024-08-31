def get_min(m, s):
    if m * 9 < s or (s == 0 and m > 1):
        return -1
    
    ans = [0] * m
    ans[-1] += 1
    s -= 1

    for i in range(len(ans)):
        if s >= 9:
            s -= 9
            ans[i] += 9
        else:
            ans[i] += s
            break

    rs = ""
    for a in ans[::-1]: rs += str(a)
    
    return rs

def get_max(m, s):
    if m * 9 < s or (s == 0 and m > 1):
        return -1

    rs = ""
    for i in range(m):
        if s >= 9:
            rs += "9"
            s -= 9
        else:
            rs += str(s)
            s -= s
    
    return rs


M, S = map(int, input().split())
print(get_min(M, S), get_max(M, S))
