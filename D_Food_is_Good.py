for i in range(int(input())):
    input()
    nums = list(map(int, input().split(" ")))

    simon = sum(nums)

    max_sum = nums[0]
    r_sum = 0
    min_idx = 0
    max_idx = 0

    for i in range(len(nums)):
        if r_sum <= 0:
            r_sum = 0
            min_idx = i
        r_sum += nums[i]
        if r_sum > max_sum:
            max_idx = i
            max_sum = r_sum
            
    if max_idx - min_idx + 1 == len(nums):
        max_sum = max(max_sum - nums[-1], max_sum - nums[0])
    
    if max_sum < simon:
        print('YES')
    else:
        print('NO')