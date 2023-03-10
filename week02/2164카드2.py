import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

deq = deque()
length = n

for i in range(1, n+1):
    deq.append(i)
    
while length > 1:
    deq.popleft()
    length -= 1
    if length == 1:
        break
    deq.append(deq.popleft())
    
print(deq.popleft())