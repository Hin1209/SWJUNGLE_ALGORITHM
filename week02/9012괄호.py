import sys

input = sys.stdin.readline

res = []
t = int(input())

def is_vps(ps):
    stack = []
    length = 0
    for i in ps:
        if i == '(':
            stack.append(i)
            length += 1
        else:
            if length == 0 or stack[-1] != '(':
                return False
            stack.pop()
            length -= 1
    if stack:
        return False
    return True

for _ in range(t):
    ps = input().rstrip()
    print('YES') if is_vps(ps) else print('NO')