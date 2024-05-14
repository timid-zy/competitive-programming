import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    nodes = []
    for i in range(n):
        nodes.append(list(map(int, input().split())))

    stack = [(0, 0)]
    min_ = float('inf')

    while stack:
        i, ops = stack.pop()
        d, [l, r] = s[i], nodes[i]
        if l == 0 and r == 0:
            min_ = min(min_, ops)
            continue

        lops = rops = ops

        if d != "R":
            rops += 1
        
        if d != "L":
            lops += 1
        
        if l > 0:
            stack.append([l - 1, lops])
        if r > 0:
            stack.append([r - 1, rops])


    # def dfs(i, ops):
    #     d, [l, r] = s[i], nodes[i]
    #     if l == 0 and r == 0:
    #         return ops

    #     lops = rops = ops
        
    #     if d != "R":
    #         rops += 1
    #     if d != "L":
    #         lops += 1
        
    #     ans = float('inf')
    #     if l != 0:
    #         ans = min(ans, dfs(l - 1, lops))
        
    #     if r != 0:
    #         ans = min(ans, dfs(r - 1, rops))
        
    #     return ans

    # print(dfs(0, 0))
    print(min_)