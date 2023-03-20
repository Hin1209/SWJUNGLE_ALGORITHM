import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
r, c = map(int, input().split())

tmp = [input().rstrip() for _ in range(r)]
world = [[0] * c for _ in range(r)]

dochi = deque()
water = deque()

for i in range(r):
    for j in range(c):
        if tmp[i][j] == 'D':
            safe = (i, j)
            world[i][j] = 100
        elif tmp[i][j] == 'X':
            world[i][j] = -1
        elif tmp[i][j] == 'S':
            world[i][j] = 1
            dochi.append((i, j, 0))
        elif tmp[i][j] == '*':
            water.append((i, j, 0))
            world[i][j] = 10

escape = -1
for time in range(2500):
    while water:
        y, x, t = water.popleft()
        if t > time:
            water.append((y, x, t))
            break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if world[ny][nx] == 0 or world[ny][nx] == 1:
                    world[ny][nx] = 10
                    water.append((ny, nx, t+1))
    while dochi:
        y, x, t = dochi.popleft()
        if t > time:
            dochi.append((y, x, t))
            break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if world[ny][nx] == 0:
                    world[ny][nx] = 1
                    dochi.append((ny, nx, t+1))
                elif world[ny][nx] == 100:
                    escape = t+1
                    break
        if escape > 0:
            break
        
    if escape > 0:
        print(escape)
        break
    
if escape < 0:
    print("KAKTUS")
    