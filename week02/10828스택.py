import sys

input = sys.stdin.readline

stack = []
n = int(input())
length = 0
res = []
for _ in range(n):
    command = list(input().split())
    if len(command) == 1:
        if command[0] == 'size':
            res.append(length)
        elif command[0] == 'top':
            if length:
                res.append(stack[-1])
            else:
                res.append(-1)
        elif command[0] == 'empty':
            if length:
                res.append(0)
            else:
                res.append(1)
        elif command[0] == 'pop':
            if length:
                res.append(stack.pop())
                length -= 1
            else:
                res.append(-1)
    else:
        num = command[1]
        if command[0] == 'push':
            stack.append(num)
            length += 1
        
for i in res:
    print(i)