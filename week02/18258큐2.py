import sys
from collections import deque

input = sys.stdin.readline

deq = deque()
length = 0

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        deq.append(command[1])
        length += 1
    elif command[0] == 'front':
        if length:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if length:
            print(deq[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(length)
    elif command[0] == 'empty':
        print(0) if length else print(1)
    elif command[0] == 'pop':
        if length:
            print(deq.popleft())
            length -= 1
        else:
            print(-1)
    