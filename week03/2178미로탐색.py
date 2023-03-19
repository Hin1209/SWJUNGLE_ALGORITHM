import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

board = [[] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    tmp = input().rstrip()
    for j in range(M):
        board[i].append(int(tmp[j]))

q = deque()
q.append((0, 0, 1))

while q:
    y, x, time = q.popleft()
    if y == N - 1 and x == M - 1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = time + 1
                q.append((ny, nx, time + 1))
                
print(visited[N - 1][M - 1])
