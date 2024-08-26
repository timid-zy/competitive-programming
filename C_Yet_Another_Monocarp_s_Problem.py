def test_answer(arr, k, hp):
    total_dmg = 0
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - prev < k:
            total_dmg += arr[i] - prev
        else:
            total_dmg += k

        prev = arr[i]
    
    return total_dmg + k >= hp


def solve(dmg, Hp):
    l, r = 1, Hp + 1
    while l < r:
        mid = l + (r - l) // 2
        if test_answer(dmg, mid, Hp):
            r = mid
        else:
            l = mid + 1
    
    return l 

for _ in range(int(input())):
    N, Hp = map(int, input().split())
    dmg = list(map(int, input().split()))
    print(solve(dmg, Hp))