s1 = input()
s2 = input()

dp = [ [0] * len(s1) for _ in range(len(s2))]

def inbound(x, y):
    return 0 <= x < len(s2) and 0 <= y < len(s1)

for i2 in range(len(s2)):
    for i1 in range(len(s1)):
        if s1[i1] == s2[i2]:
            dp[i2][i1] = dp[i2-1][i1-1] + 1 if inbound(i2-1, i1-1) else 1
            continue

        left = dp[i2][i1-1] if inbound(i2, i1-1) else 0
        up = dp[i2-1][i1] if inbound(i2-1, i1) else 0
        dp[i2][i1] = max(left, up)

ans = []
r, c = len(s2) - 1, len(s1) - 1

while len(ans) < dp[-1][-1]:
    if s2[r] == s1[c]:
        ans.append(s2[r])
        r -= 1
        c -= 1
    
    else:
        if not inbound(r-1, c):
            c -= 1
        elif not inbound(r, c-1):
            r -= 1
        elif dp[r-1][c] > dp[r][c-1]:
            r -= 1
        else:
            c -= 1

print("".join(ans[::-1]))