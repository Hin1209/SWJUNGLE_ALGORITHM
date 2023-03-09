import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

size = int(input())

col = [0 for _ in range(size)]
row = [0 for _ in range(size)]
diagonal_p = [0 for _ in range(2 * size)]
diagonal_m = [0 for _ in range(2 * size)]

def find_perfect(state):
    res = 0
    if state == size:
        return 1
    else:
        for i in range(size):
            if col[i]:
                continue
            check_diagonal_p = state + (size - i)
            check_diagonal_m = i + state 
            if diagonal_p[check_diagonal_p]:
                continue
            if diagonal_m[check_diagonal_m]:
                continue
            col[i] = 1
            diagonal_p[check_diagonal_p] = 1
            diagonal_m[check_diagonal_m] = 1
            res += find_perfect(state+1)
            col[i] = 0
            diagonal_p[check_diagonal_p] = 0
            diagonal_m[check_diagonal_m] = 0
            
        return res
        
print(find_perfect(0))