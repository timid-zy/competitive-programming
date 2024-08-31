from collections import deque

E = int(input())
adj = [[] for _ in range(E)]

for _ in range(E - 1):
    x, y = list(map(int, input().split()))
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)

level = 0
queue = deque([0])
visited = set([0])
a = b = 0

while queue:
    if level % 2 == 0:
        a += len(queue)
    else:
        b += len(queue)
    
    for i in range(len(queue)):
        n = queue.popleft()
        for ed in adj[n]:
            if ed not in visited:
                queue.append(ed)
                visited.add(ed)
    
    level += 1


print((a * b) - (E - 1))