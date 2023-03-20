import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
box = []
visited = [[0] * M for _ in range(N)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    box.append(tmp)

q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = 0
            q.append((i, j, 0))

while q:
    y, x, time = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if box[ny][nx] == 0:
                box[ny][nx] = 1
                visited[ny][nx] = time + 1
                q.append((ny, nx, time + 1))

result = 0
perfect = 1
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            perfect = 0
            break
        if visited[i][j] > result:
            result = visited[i][j]

if perfect:
    print(result)
else:
    print(-1)