for i in range(int(input())):
    input()
    arr = list(map(int, input().split(" ")))
    
    sorted_arr = sorted(arr)

    max_num = sorted_arr[-1]
    max_count = sorted_arr.count(max_num)
    second_max = sorted_arr[-1* max_count - 1] if max_count < len(arr) else None

    ret_str = ""
    for i in range(len(arr)):
        if arr[i] == max_num:

            if max_count > 1:
                ret_str += "0 "
            
            else:
                ret_str += str(arr[i] - second_max) + " "
        
        else:
            ret_str += str(arr[i] - max_num) + " "
    print(ret_str)