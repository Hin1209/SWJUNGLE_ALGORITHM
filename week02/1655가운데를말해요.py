import sys
import heapq

input = sys.stdin.readline

n = int(input())

high = []
low = []

for _ in range(n):
    num = int(input())
    if len(low) == 0 and len(high) == 0:
        heapq.heappush(low, -num)
        print(num)
        continue
    if -low[0] <= num:
        heapq.heappush(high, num)
    else:
        heapq.heappush(low, -num)
    if len(low) - len(high) > 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) - len(low) > 1:
        heapq.heappush(low, -heapq.heappop(high))
    if len(low) >= len(high):
        print(-low[0])
    else:
        print(high[0])
        