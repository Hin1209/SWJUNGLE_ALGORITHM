import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x, visited):
    deq = deque()
    deq.append((y, x))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and world[ny][nx] > 0:
                    visited[ny][nx] = 1
                    deq.append((ny, nx))

dic = {}
for i in range(n):
    for j in range(m):
        if world[i][j] > 0:
            dic[(i, j)] = world[i][j]
            
time = 1
while True:
    loop = list(dic.keys())
    for y, x in loop:
        cnt = 0
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if world[ny][nx] == 0:
                    cnt += 1
        dic[(y,x)] -= cnt 
    not_exist = True
    for y, x in loop:
        if dic[(y, x)] <= 0: 
            world[y][x] = 0
            dic.pop((y, x))
        else:
            not_exist = False
    if not_exist:
        print(0)
        break
    visited = [[0] * m for _ in range(n)]
    cnt_dfs = 0
    for y, x in dic.keys():
        if not visited[y][x]:
            if cnt_dfs == 1:
                cnt_dfs += 1
                break
            bfs(y, x, visited)
            cnt_dfs += 1
    if cnt_dfs > 1:
        print(time)
        break
    time += 1 
    
    