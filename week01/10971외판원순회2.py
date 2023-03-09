import sys
from itertools import permutations

input = sys.stdin.readline

   
n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]

candidates = permutations(range(n), n)

res = int(1e9)
for candidate in candidates:
    tmp = 0
    for i in range(n-1):
        now = candidate[i]
        next_city = candidate[i+1]
        if cost[now][next_city]:
            tmp += cost[now][next_city]
        else:
            tmp += int(1e9)
    last = cost[candidate[-1]][candidate[0]]
    tmp += last if last else int(1e9)
    if tmp < res:
        res = tmp
        
print(res)
        