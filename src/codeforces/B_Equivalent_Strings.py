import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def least(s):
        if len(s) % 2 == 1:
            return s

        s1 = least(s[:len(s)//2])
        s2 = least(s[len(s)//2:])
        if s1 > s2:
            return s2 + s1
        
        return s1 + s2
        

    def solve():
        a, b = input(), input()
        if least(a) == least(b):
            print("YES")
        else:
            print("NO")

    solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


