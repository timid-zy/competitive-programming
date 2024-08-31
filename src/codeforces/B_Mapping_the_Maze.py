import sys
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for _ in range(E):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)

zeroes = 0
ones = 0
twos = 0
more = 0
count = 0

stack = [0]
visited = set([0])
while stack:
    count += 1
    n = stack.pop()
    if len(adj[n]) == 1:
        ones += 1
    
    elif len(adj[n]) == 2:
        twos += 1
    
    elif len(adj[n]) == 0:
        zeroes += 1
    
    else:
        more += 1
    
    for ed in adj[n]:
        if ed not in visited:
            visited.add(ed)
            stack.append(ed)

if ones == 2 and twos == count - ones:
    print('bus topology')

elif twos == count:
    print('ring topology')

elif more == 1 and ones == count - more:
    print('star topology')

else:
    print('unknown topology')