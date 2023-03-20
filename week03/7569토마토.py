import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))
    
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

deq = deque()

max_time = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                deq.append((i, j, k, 0))
                visited[i][j][k] = 1
        
while deq:
    z, y, x, t = deq.popleft()
    for i in range(6):
        nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if box[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                box[nz][ny][nx] = 1
                visited[nz][ny][nx] = 1
                deq.append((nz, ny, nx, t+1))
                max_time = max(max_time, t+1)

not_possible = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                not_possible = True

print(max_time) if not not_possible else print(-1)