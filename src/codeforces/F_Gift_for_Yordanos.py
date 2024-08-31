import sys, threading
import functools

input = lambda: sys.stdin.readline().strip()

def main():
    s = input()

    @functools.lru_cache
    def findMin(idx=0, t=[], u=[]):
        nonlocal s
        if idx == len(s) and len(t) == 0:
            return u
        elif len(t) == 0:
            t.append(s[idx])
            return findMin(idx + 1, t, u)
        elif idx == len(s):
            last_el = t.pop()
            u.append(last_el)
            return findMin(idx, t, u)

        t.append(s[idx])
        possibility1 = findMin(idx + 1, t, u)
        t.pop()
        last_el = t.pop()
        u.append(last_el)
        possibility2 = findMin(idx, t, u)
        
        return min(possibility1, possibility2)
    
    res = findMin()
    print("".join(res))
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()