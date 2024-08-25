N, M = map(int, input().split())
cols = list(map(int, input().split()))
prefix = [0] * len(cols)
postfix = [0] * len(cols)

for i in range(1, len(cols)):
    prefix[i] = prefix[i-1] + max(0, -1 * (cols[i] - cols[i-1]))

for i in range(len(cols) - 2, -1, -1):
    postfix[i] = postfix[i+1] + max(0, -1 * (cols[i] - cols[i+1]))

for _ in range(M):
    s, t = map(int, input().split())
    if s <= t:
        print(prefix[t-1] - prefix[s-1])
    else:
        print(postfix[t-1] - postfix[s-1])
