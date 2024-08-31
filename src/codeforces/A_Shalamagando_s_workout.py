n = input()
arr = list(map(int, input().split()))

ans = [0, 0, 0]
for i in range(len(arr)):
    ans[i % 3] += arr[i]

idx = 0
max_ = ans[0]
for i in range(1, len(ans)):
    if max_ < ans[i]:
        max_ = ans[i]
        idx = i

if idx == 0:
    print('chest')

elif idx == 1:
    print('biceps')

else:
    print('back')