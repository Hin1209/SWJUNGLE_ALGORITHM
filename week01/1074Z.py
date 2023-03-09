import sys

input = sys.stdin.readline

def search_z(sx, sy, ex, ey):
    global r, c, cnt
    mx = (ex + sx) // 2
    my = (ey + sy) // 2
    size = ((ex - sx) // 2) ** 2
    nsx = sx; nsy = sy; nex = ex; ney = ey
    cx = 0; cy = 0
    if size == 1:
        for i in range(2):
            for j in range(2):
                if sx + j == c and sy + i == r:
                    cnt += 1
                    return True
                else:
                    cnt += 1
    if r < my:
        ney = my
    else:
        nsy = my
        cy = 1
    if c < mx:
        nex = mx
    else:
        nsx = mx
        cx = 1
    if cx == 1 and cy == 1:
        cnt += 3 * size
    elif cx == 1 and cy == 0:
        cnt += size
    elif cx == 0 and cy == 1:
        cnt += 2 * size
    search_z(nsx, nsy, nex, ney)

N, r, c = map(int, input().split())
cnt = -1
search_z(0, 0, 2 ** N, 2 ** N)
print(cnt)
