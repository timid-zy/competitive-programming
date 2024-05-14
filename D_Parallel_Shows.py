shows = []

for i in range(int(input())):
    show = list(map(int, input().split()))
    shows.append(show)

def returnStartTime(arr): return arr[0]
shows.sort(key=returnStartTime)

# end times
firstTV = -1
secondTV = -1
flag = True

for i in range(len(shows)):
    startTime, endTime = shows[i]
    # print(startTime, endTime, firstTV, secondTV)
    if startTime > firstTV:
        firstTV = endTime
    elif startTime > secondTV:
        secondTV = endTime
    else:
        flag = False
        break

if flag: print('YES')
else: print('NO')