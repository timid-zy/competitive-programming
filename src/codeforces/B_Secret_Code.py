from collections import deque

N = int(input())
r = N % 2 == 1
S = input()
deq = deque()
for c in S:
    if r:
        deq.append(c)
        r = not r
        continue

    deq.appendleft(c)
    r = not r

res = []
while deq:
    res.append(deq.popleft())

print("".join(res))