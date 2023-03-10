import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())
k = int(input())

world = [[0] * n for _ in range(n)]
world[0][0] = 1

direction = 0

for _ in range(k):
    y, x = map(int, input().split())
    world[y-1][x-1] = 2

L = int(input())

change_info = [0] * 10001
for _ in range(L):
    t, d = input().split()
    t = int(t) + 1
    if d == 'L':
        d = -1
    elif d == 'D':
        d = 1
    change_info[t] = d
    
length = 0
deq = deque()
deq.append((0, 0))

for i in range(1, 10001):
    direction = (direction + change_info[i]) % 4
    head = deq[0]
    ny, nx = head[0]+dy[direction], head[1]+dx[direction]
    if 0 <= ny < n and 0 <= nx < n:
        if world[ny][nx] == 2:
            deq.appendleft((ny, nx))
            world[ny][nx] = 1
        elif world[ny][nx] == 0:
            deq.appendleft((ny, nx))
            tail_y, tail_x = deq.pop()
            world[ny][nx] = 1
            world[tail_y][tail_x] = 0
        elif world[ny][nx] == 1:
            print(i)
            break
    else:
        print(i)
        break