from collections import deque

def bfs(queue, rem, ans):
    lvl = 1
    visited = set(queue)
    while len(queue) > 0:
        for _ in range(len(queue)):
            curr = queue.popleft()

            for ed in adj[curr]:
                if ed not in visited:
                    if arr[ed] % 2 == rem:
                        ans[ed] = str(lvl)
                    visited.add(ed)
                    queue.append(ed)

        lvl += 1


V = int(input())
arr = list(map(int, input().split()))

adj = [[] for _ in range(V)]
even = deque()
odd = deque()
for i in range(V):
    if arr[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

    l, r = i - arr[i], i + arr[i]
    if l >= 0:
        adj[l].append(i)
    
    if r < len(arr):
        adj[r].append(i)


ans = ["-1"] * V
bfs(even, 1, ans)
bfs(odd, 0, ans)

print(" ".join(ans))