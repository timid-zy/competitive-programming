input()
time = list(map(int, input().split(" ")))
time.sort()

waited = 0
count = 0
for i in range(len(time)):
    if time[i] >= waited:
        count += 1
        waited += time[i]
        

print(count)