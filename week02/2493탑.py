import sys

input = sys.stdin.readline

n = int(input())

top = list(map(int, input().split()))
receiver = [0] * n

stack = []

for i in range(n):
    if len(stack) == 0:
        stack.append((top[i], i+1))
        receiver[i] = 0
        continue
    while len(stack) > 0 and stack[-1][0] < top[i]:
        stack.pop()
    if len(stack) == 0:
        receiver[i] = 0
    else:
        receiver[i] = stack[-1][1]
    stack.append((top[i], i+1))
    
print(*receiver)