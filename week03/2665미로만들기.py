import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n = int(input())

INF = int(1e9)
world = [input().rstrip() for _ in range(n)]
visited = [[INF] * n for _ in range(n)]

deq = deque()
deq.append((0, 0, 0))

while deq:
    y, x, black = deq.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if world[ny][nx] == '1':
                if visited[ny][nx] > black:
                    visited[ny][nx] = black
                    deq.append((ny, nx, black))
            elif world[ny][nx] == '0':
                if visited[ny][nx] > black + 1:
                    visited[ny][nx] = black + 1
                    deq.append((ny, nx, black+1))
                    
print(visited[n-1][n-1])