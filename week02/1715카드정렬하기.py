import sys
import heapq

input = sys.stdin.readline

n = int(input())

h = []

for _ in range(n):
    heapq.heappush(h, int(input()))
    
res = 0
while len(h) > 1:
    num1 = heapq.heappop(h)
    num2 = heapq.heappop(h)
    res += (num1 + num2)
    heapq.heappush(h, num1+num2)

print(res)