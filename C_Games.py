def get(arr, i):
    if i < 0: return 0
    return arr[i]

def solve():
    input()
    A = list(map(int, input().split()))
    even, odd = [], []
    for n in A:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    
    even.sort()
    odd.sort()

    al, bo = len(even) - 1, len(odd) - 1
    score = 0
    t_alice = True
    for __ in range(len(A)):
        moves = [
                get(even, al) - max(get(even, al-1), get(odd, bo)),
                get(odd, bo) - max(get(odd, bo-1), get(even, al))
            ]
        
        if t_alice:
            if moves[0] > moves[1]:
                score += get(even, al)
                al -= 1
            else:
                bo -= 1
        
        else:
            if moves[0] < moves[1]:
                score -= get(odd, bo)
                bo -= 1
            else:
                al -= 1
        
        t_alice = not t_alice
    
    return "Alice" if score > 0 else "Bob" if score < 0 else "Tie"



for _ in range(int(input())):
    print(solve())

# 5 2 7 3

# hit:
    # op take: +j-1
    # op hit: -i

# taker: +i
    # op take: +j
    # op hit: -(i-1)