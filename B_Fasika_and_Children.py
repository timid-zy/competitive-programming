from math import ceil

_, candy = map(int, input().split())
ans_i, ans = 0, float("-inf")
children = list(map(int, input().split()))
for i in range(len(children)):
    curr = ceil(children[i] / candy)
    if curr >= ans:
        ans = curr
        ans_i = i

print(ans_i + 1)