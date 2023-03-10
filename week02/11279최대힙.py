import sys
import heapq

input = sys.stdin.readline

h = []

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -num)