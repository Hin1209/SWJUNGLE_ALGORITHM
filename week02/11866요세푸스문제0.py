import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque()
res = []

for i in range(1, n+1):
    deq.append(i)
    
while deq:
    cnt = 1
    while cnt < k:
        cnt += 1
        deq.append(deq.popleft())
    res.append(deq.popleft())

print('<', end="")
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end=">")
    else:
        print('{},'.format(res[i]), end=" ")
