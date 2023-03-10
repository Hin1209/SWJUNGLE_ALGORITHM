import sys
import heapq

input = sys.stdin.readline

n = int(input())

pos_info = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o: h, o = o, h
    heapq.heappush(pos_info, (o, h))

d = int(input())

max_cnt = 0
cnt = 0
happy = []

while pos_info:
    o, h = heapq.heappop(pos_info)
    if o - d <= h:
        heapq.heappush(happy, (h, o))
        cnt += 1
    while happy:
        happy_h, happy_o = heapq.heappop(happy)
        if happy_h < o - d:
            cnt -= 1
        else:
            heapq.heappush(happy, (happy_h, happy_o))
            break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)