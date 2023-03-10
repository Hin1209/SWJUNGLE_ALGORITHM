import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()

stack = []

remove = []

for i in range(n):
    integer_num = int(num[i])
    if len(stack) == 0:
        stack.append(integer_num)
    else:
        while len(stack) > 0 and stack[-1] < integer_num and len(remove) < k:
            remove.append(stack.pop())
        stack.append(integer_num)

while len(remove) < k:
    remove.append(stack.pop())
    
for i in stack:
    print(i, end="")