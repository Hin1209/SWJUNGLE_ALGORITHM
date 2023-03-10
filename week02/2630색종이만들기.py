import sys

input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

def check(y, x, size):
    if size == 1:
        return True
    cnt_white = 0
    cnt_blue = 0
    for i in range(y, y+size):
        for j in range(x, x+size):
            if paper[i][j] == 1: cnt_blue += 1
            elif paper[i][j] == 0: cnt_white += 1
    if cnt_white != 0 and cnt_blue != 0:
        return False
    else:
        return True

def divide_paper(y, x, size):
    res = [0, 0]
    if check(y, x, size):
        res[paper[y][x]] += 1
        return res
    
    mid_x = x + size // 2
    mid_y = y + size // 2
    tmp = divide_paper(y, x, size // 2)
    res[0] += tmp[0]
    res[1] += tmp[1]
    tmp = divide_paper(y, mid_x, size // 2)
    res[0] += tmp[0]
    res[1] += tmp[1]
    tmp = divide_paper(mid_y, x, size // 2)
    res[0] += tmp[0]
    res[1] += tmp[1]
    tmp = divide_paper(mid_y, mid_x, size // 2)
    res[0] += tmp[0]
    res[1] += tmp[1] 
    return res

ans = divide_paper(0, 0, n)
for i in ans:
    print(i)