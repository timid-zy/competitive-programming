import bisect
_, b = list(map(int, input().split()))
spaceships = list(map(int, input().split()))
bases = []
for i in range(b):
    bases.append(tuple(map(int, input().split())))

bases.sort(key=lambda x: x[0])

defense = []
for i in range(len(bases)):
    defense.append(bases[i][0])

gold = [bases[0][1]]
for i in range(1, len(bases)):
    gold.append(gold[-1] + bases[i][1])

s = ""
for i in range(len(spaceships)):
    if spaceships[i] < defense[0]:
        s += "0 "
    else:
        s += str(gold[bisect.bisect_right(defense, spaceships[i]) - 1]) + " "

print(s)