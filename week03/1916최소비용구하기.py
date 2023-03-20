import sys
import heapq
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

city = int(input())
bus = int(input())

moving_cost = [[] for _ in range(city+1)]
INF = 1e9
best_cost = [INF] * (city+1)


for i in range(bus):
    start, end, cost = map(int, input().split())
    moving_cost[start].append((end, cost))

travel_start, destination = map(int, input().split())

heap = []
best_cost[travel_start] = 0
heapq.heappush(heap, (0, travel_start))

while heap:
    cost, pos = heapq.heappop(heap)
    if pos == destination:
        break
    for next, next_cost in moving_cost[pos]:
        if best_cost[next] > cost + next_cost:
            best_cost[next] = cost + next_cost
            heapq.heappush(heap, (best_cost[next], next))
        
print(best_cost[destination])